Summary:	Phun is a free game like 2D physics sandbox
Summary(hu.UTF-8):	Phun egy 2D fizikai játszótér
Name:		phun
Version:	5.28
Release:	0.1
License:	other
Group:		Applications
Source0:	http://www.phunland.com/download/Phun_beta_5_28_linux32.tgz
# Source0-md5:	aade8e21f278cd386aa6143eaa16cf7c
Source1:	http://www.phunland.com/download/Phun_beta_5_28_linux64.tgz
# Source1-md5:	ff262b43cde833cbef0c3ef4f61287e7
Source2:	%{name}
Source3:	%{name}.desktop
URL:		http://www.phunland.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phun is a free game like 2D physics sandbox.

%description -l hu.UTF-8
Phun egy 2D fizikai játszótér.

%prep
%ifarch %{x8664}
%setup -q -T -n Phun -b1
%else
%setup -q -T -n Phun -b0
%endif

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_desktopdir}

cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phun
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
