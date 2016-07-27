%{?scl:%scl_package high-scale-lib}
%{!?scl:%global pkg_name %{name}}

Name: %{?scl_prefix}jopt-simple
Version: 4.6
Release: 1%{?dist}
Summary: A Java command line parser
License: MIT
URL: http://pholser.github.io/jopt-simple/
Source0: https://github.com/pholser/jopt-simple/archive/jopt-simple-%{version}.tar.gz

BuildArch: noarch

BuildRequires: %{?scl_mvn_prefix}maven-local
BuildRequires: %{?scl_mvn_prefix}joda-time

%description
JOpt Simple is a Java library for parsing command line options, such as those
you might pass to an invocation of javac.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%{?scl_enable}
%setup -q -n jopt-simple-jopt-simple-%{version}

%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_dep org.infinitest:continuous-testing-toolkit
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%{?scl_disable}

%build
%{?scl_enable}
# Unit testing is disabled due to a missing dependency in Fedora of continuous-testing-toolkit
%mvn_build -f
%{?scl_disable}

%install
%{?scl_enable}
%mvn_install
%{?scl_disable}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Jul 27 2016 Pavel Raiskup <praiskup@redhat.com> - 4.6-1
- sclize
