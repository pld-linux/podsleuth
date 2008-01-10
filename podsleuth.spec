%include	/usr/lib/rpm/macros.mono
Summary:	A tool to discover detailed model information about iPods
Name:		podsleuth
Version:	0.6.1
Release:	1
# no real license information, just included COPYING
License:	LGPL v2
Group:		Libraries
Source0:	http://banshee-project.org/files/podsleuth/%{name}-%{version}.tar.bz2
# Source0-md5:	201f779f2a8d8cf71d1cf4e7d1b798c7
URL:		http://banshee-project.org/PodSleuth
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	hal-devel >= 0.5.6
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sg3_utils-devel
Obsoletes:	libipoddevice
ExcludeArch:	i386
# can't be noarch because of pkgconfigdir (use /usr/share/pkgconfig?)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodSleuth is a tool to discover detailed model information about an Apple (TM) iPod (TM). Its primary role is to be run as a callout by HAL because root access is needed to scan the device for required information. When the model information is discovered, it is merged into HAL as properties for other applications to use.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/podsleuth
%attr(755,root,root) %{_libdir}/hal/hal-podsleuth
%{_datadir}/hal/fdi/policy/20thirdparty/20-podsleuth.fdi
%{_libdir}/podsleuth
%{_pkgconfigdir}/podsleuth.pc
