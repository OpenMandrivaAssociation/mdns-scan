Summary:	Tool for scanning mDNS/DNS-SD published services in local network
Name:		mdns-scan
Version:	0.5
Release:	2
License:	GPLv2+
Group:		Networking/Other
Url:		https://freecode.com/projects/mdns-scan
Source0:	http://0pointer.de/lennart/projects/mdns-scan/mdns-scan-%{version}.tar.gz

%description
mdns-scan is a tool for scanning for mDNS/DNS-SD published services
on the local network. It issues a mDNS PTR query to the special RR
_services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

