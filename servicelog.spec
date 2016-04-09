Summary:	Servicelog tools
Summary(pl.UTF-8):	Narzędzia do obsługi logu serwisowego
Name:		servicelog
Version:	1.1.14
Release:	1
License:	GPL v2+ with librtas exception
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
# Source0-md5:	2435b739238b1dfb018d04b96416e4a8
URL:		http://linux-diag.sourceforge.net/servicelog/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libservicelog-devel
BuildRequires:	libtool
# relies on ppc-specific libservicelog
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Servicelog contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%description -l pl.UTF-8
Działające z linii poleceń narzędzia do przeglądania i obróbki
zawartości bazy danych logu serwisowego (servicelog). Baza ta zawiera
wpisy przydatne przy wykonywaniu operacji serwisowych oraz udostępnia
historię operacji serwisowych wykonywanych w systemie.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/log_repair_action
%attr(755,root,root) %{_bindir}/servicelog
%attr(755,root,root) %{_bindir}/servicelog_manage
%attr(755,root,root) %{_bindir}/servicelog_notify
%attr(755,root,root) %{_bindir}/v1_servicelog
%attr(755,root,root) %{_bindir}/v29_servicelog
%attr(755,root,root) %{_sbindir}/slog_common_event
%{_mandir}/man8/log_repair_action.8*
%{_mandir}/man8/servicelog.8*
%{_mandir}/man8/servicelog_manage.8*
%{_mandir}/man8/servicelog_notify.8*
