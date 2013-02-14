# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
Name: jopt-simple
Version: 3.3
Release: 8%{?dist}
Summary: A Java command line parser
License: MIT
Group: Development/Libraries
URL: http://jopt-simple.sourceforge.net
# https://github.com/pholser/jopt-simple/tarball/jopt-simple-3.3
Source0: https://download.github.com/pholser-jopt-simple-jopt-simple-%{version}-0-g59a05aa.tar.gz
Patch0: jopt-simple-buildfixes.patch
BuildArch: noarch
BuildRequires: jpackage-utils
BuildRequires: java-devel >= 1.5.0
BuildRequires: maven-local maven-scm
BuildRequires: maven-enforcer-plugin maven-dependency-plugin
Requires: java >= 0:1.5.0
Requires: jpackage-utils
# Unit testing is disabled due to missing dependencies.
#BuildRequires:  joda-time
#BuildRequires:  junit4
#BuildRequires:  continuous-testing-toolkit
#BuildRequires:  ant

%description
A Java library for parsing command line options.

%package javadoc
Summary: Javadoc for %{name}
Group: Documentation
Requires: jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n pholser-jopt-simple-9d4f1b6
%patch0 -p1 -b .buildfixes

%build
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.skip=true

%install
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rf target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.3-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Karel Klíč <kklic@redhat.com> - 3.3-5
- Added maven-enforcer-plugin and maven-dependency-plugin as build
  requires to fix the build process (although not sure why that is
  neccessary)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Karel Klíč <kklic@redhat.com> - 3.3-3
- Include the license text in the javadoc package, which is
  independent from the main package
- Use %%add_maven_depmap instead of %%add_to_maven_depmap

* Fri Jul 29 2011 Karel Klíč <kklic@redhat.com> - 3.3-2
- Use %%{_mavenpomdir} instead of %%{_datadir}/maven2/poms
- Removed %%post(un) %%update_maven_depmap calls, not needed in F-15+

* Wed Jun 29 2011 Karel Klíč <kklic@redhat.com> - 3.3-1
- Use maven3 instead of maven2 to build the package.
- Updated to upstream final 3.3 release.

* Thu Apr 28 2011 Karel Klíč <kklic@redhat.com> - 3.3-0.2.git12c0e63
- Added jpackage-utils dependency to -javadoc package (needed for directory)
- Better versioning

* Tue Apr 26 2011 Karel Klíč <kklic@redhat.com> - 3.3-0.1.git12c0e63
- Repackaged to follow Fedora guidelines
- Upstream version 3.2 source code seems not to be available,
  3.3-SNAPSHOT is available in git and seems stable

* Tue Aug 18 2009 Ralph Apel <r.apel@r-apel.de> - 0:3.1-1
- first release
