Name:		mdns-scan
Summary:	Tool for scanning mDNS/DNS-SD published services in local network
Group:		Networking/Other
Version:	0.4
Release:	1
License:	GPL
URL:		http://freecode.com/projects/mdns-scan
Source0:	http://0pointer.de/lennart/projects/mdns-scan/mdns-scan-0.4.tar.gz
Patch0:		mdns-scan-0.4-add-manual.patch
#BuildRequires:


%description
mdns-scan is a tool for scanning for mDNS/DNS-SD published services
on the local network. It issues a mDNS PTR query to the special RR
_services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%prep
%setup -q
%apply_patches

%build
%make

%install
rm -fr %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall_std



%changelog
* Thu Jan 26 2012 Guilherme Moro <guilherme@mandriva.com> 0.4-1
+ Revision: 769176
- imported package mdns-scan


* Thu Jan 26 2012 Zé <ze@mandriva.org> 4.8.40-6-mde
- first package
