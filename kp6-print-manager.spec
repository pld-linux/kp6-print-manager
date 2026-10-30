%define		kframever	6.14.0
%define		qtver		6.9.1
%define		kaname		print-manager
Summary:	Print manager
Name:		kp6-%{kaname}
Version:	6.8.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/plasma/%{version}/%{kaname}-%{version}.tar.xz
# Source0-md5:	6834c8f81334d3bd19ef1ed526ec9bbe
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kirigami-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kp6-libplasma-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for managing print jobs and printers.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/configure-printer
%attr(755,root,root) %{_bindir}/plasma-print-queue
%{_libdir}/libkcups.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.printmanager.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_printer_manager.so
%{_libdir}/qt6/plugins/kf6/kded/printmanager.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/printmanager
%{_libdir}/qt6/qml/org/kde/plasma/printmanager/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/printmanager/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/printmanager/kcups.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/printmanager/libkcupsplugin.so
%{_desktopdir}/kcm_printer_manager.desktop
%{_desktopdir}/org.kde.ConfigurePrinter.desktop
%{_desktopdir}/org.kde.plasma.printqueue.desktop
%{_datadir}/knotifications6/printmanager.notifyrc
%{_datadir}/qlogging-categories6/pmlogs.categories
%{_datadir}/metainfo/org.kde.print-manager.metainfo.xml
