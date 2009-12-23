%include	/usr/lib/rpm/macros.mono
Summary:	A tool to discover detailed model information about iPods
Summary(pl.UTF-8):	Narzędzie do odczytu szczegółowych informacji o modelu iPoda
Name:		podsleuth
Version:	0.6.5
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://banshee-project.org/files/podsleuth/0.6.5/%{name}-%{version}.tar.bz2
# Source0-md5:	5cbe9c3bb199912e15f65314b4f46ca8
Source1:	org.podsleuth.conf
Patch0:		%{name}-pmake.patch
Patch1:		%{name}-nodebug.patch
URL:		http://banshee-project.org/PodSleuth
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	hal-devel >= 0.5.6
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sg3_utils-devel >= 1.27
Requires:	hal >= 0.5.6
# DllImport, not detected by monoautodeps
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Requires:	libsgutils2.so.2()(64bit)
%else
Requires:	libsgutils2.so.2
%endif
# doesn't conflict with libipoddevice - either obsolete all libipoddevice* packages, or nothing
#Obsoletes:	libipoddevice
ExcludeArch:	i386
# can't be noarch because of pkgconfigdir (use /usr/share/pkgconfig?)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodSleuth is a tool to discover detailed model information about an
Apple(TM) iPod(TM). Its primary role is to be run as a callout by
HAL because root access is needed to scan the device for required
information. When the model information is discovered, it is merged
into HAL as properties for other applications to use.

%description -l pl.UTF-8
PodSleuth to narzędzie do odczytu szczegółowych informacji o modelu
urządzenia Apple(TM) iPod(TM). Jest przeznaczony głównie do
wywoływania przez HAL-a, ponieważ do odczytu wymaganych informacji z
urządzenia potrzebne są uprawnienia roota. Po odczycie informacji o
modelu są one włączane do HAL-a jako właściwości do wykorzystania
przez inne aplikacje.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

install -d $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install  %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/podsleuth
%attr(755,root,root) %{_libdir}/hal/hal-podsleuth
%{_datadir}/hal/fdi/policy/20thirdparty/20-podsleuth.fdi
# TODO: *.mdb to -debug or /dev/null?
/usr/lib/podsleuth
%{_pkgconfigdir}/podsleuth.pc
%{_sysconfdir}/dbus-1/system.d/org.podsleuth.conf
