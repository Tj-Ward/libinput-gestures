Name:           libinput-gestures
Version:        2.80
Release:        2%{?dist}

Summary:        Actions gestures on your touchpad using libinput

License:        GPLv3+
URL:            https://github.com/bulletmark/libinput-gestures
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  systemd

Requires:       libinput, libinput-utils
Requires:       python3 >= 3.8
Requires:       wmctrl
Requires:       xdotool

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad
and maps them to gestures you configure in a configuration file. Each gesture
can be configured to activate a shell command which is typically an xdotool
command to action desktop/window/application keyboard combinations and commands.

%prep
%autosetup

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-setup
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.svg
%{_userunitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Thu 2025 Tj-Ward <tjw.ward@gmail.com> - 2.80-1
- Initial commit
