#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-systemmonitor
Version  : 6.0.2
Release  : 44
URL      : https://download.kde.org/stable/plasma/6.0.2/plasma-systemmonitor-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/plasma-systemmonitor-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/plasma-systemmonitor-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: plasma-systemmonitor-bin = %{version}-%{release}
Requires: plasma-systemmonitor-data = %{version}-%{release}
Requires: plasma-systemmonitor-lib = %{version}-%{release}
Requires: plasma-systemmonitor-license = %{version}-%{release}
Requires: plasma-systemmonitor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdeplasma-addons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kirigami-addons-dev
BuildRequires : kirigami-dev
BuildRequires : ksystemstats
BuildRequires : libksysguard-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
plasma-systemmonitor
====================
An application for monitoring system resources.

%package bin
Summary: bin components for the plasma-systemmonitor package.
Group: Binaries
Requires: plasma-systemmonitor-data = %{version}-%{release}
Requires: plasma-systemmonitor-license = %{version}-%{release}

%description bin
bin components for the plasma-systemmonitor package.


%package data
Summary: data components for the plasma-systemmonitor package.
Group: Data

%description data
data components for the plasma-systemmonitor package.


%package dev
Summary: dev components for the plasma-systemmonitor package.
Group: Development
Requires: plasma-systemmonitor-lib = %{version}-%{release}
Requires: plasma-systemmonitor-bin = %{version}-%{release}
Requires: plasma-systemmonitor-data = %{version}-%{release}
Provides: plasma-systemmonitor-devel = %{version}-%{release}
Requires: plasma-systemmonitor = %{version}-%{release}

%description dev
dev components for the plasma-systemmonitor package.


%package lib
Summary: lib components for the plasma-systemmonitor package.
Group: Libraries
Requires: plasma-systemmonitor-data = %{version}-%{release}
Requires: plasma-systemmonitor-license = %{version}-%{release}

%description lib
lib components for the plasma-systemmonitor package.


%package license
Summary: license components for the plasma-systemmonitor package.
Group: Default

%description license
license components for the plasma-systemmonitor package.


%package locales
Summary: locales components for the plasma-systemmonitor package.
Group: Default

%description locales
locales components for the plasma-systemmonitor package.


%prep
%setup -q -n plasma-systemmonitor-6.0.2
cd %{_builddir}/plasma-systemmonitor-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710366335
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710366335
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-systemmonitor
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-systemmonitor-%{version}/logo.png.license %{buildroot}/usr/share/package-licenses/plasma-systemmonitor/ce37caa1aac2e9037a7c5648a7519d5bb0970ed3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ksysguard_face_org.kde.ksysguard.applicationstable
%find_lang ksysguard_face_org.kde.ksysguard.processtable
%find_lang plasma-systemmonitor
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/ksysguard/page/ColumnControl.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/ConditionalLoader.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/Container.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/DialogLoader.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/EditablePage.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/EditablePageAction.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/EditorToolBar.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/FaceConfigurationPage.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/FaceControl.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/LoadPresetDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/MissingSensorsDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/MoveButton.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PageContents.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PageDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PageEditor.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PageSortDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PlaceholderRectangle.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/PlasmaSystemMonitorPage.qmltypes
/usr/lib64/qt6/qml/org/kde/ksysguard/page/RowControl.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/SectionControl.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/page/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/ksysguard/page/qmldir
/usr/lib64/qt6/qml/org/kde/ksysguard/table/BaseCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/BaseTableView.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/ColumnConfigurationDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/FirstCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/KillDialog.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/LineChartCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/PlasmaSystemMonitorTable.qmltypes
/usr/lib64/qt6/qml/org/kde/ksysguard/table/TableViewHeader.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/TextCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/UserCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/table/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/ksysguard/table/qmldir

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/plasma-systemmonitor
/usr/bin/plasma-systemmonitor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.plasma-systemmonitor.desktop
/usr/share/config.kcfg/systemmonitor.kcfg
/usr/share/kglobalaccel/org.kde.plasma-systemmonitor.desktop
/usr/share/knsrcfiles/plasma-systemmonitor.knsrc
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/ApplicationDetails.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/ApplicationInformation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/ApplicationsTableView.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/contents/ui/LineChartCard.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/contents/ui/ProcessTableView.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.processtable/metadata.json
/usr/share/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
/usr/share/plasma-systemmonitor/applications.page
/usr/share/plasma-systemmonitor/history.page
/usr/share/plasma-systemmonitor/overview.page
/usr/share/plasma-systemmonitor/processes.page
/usr/share/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libPlasmaSystemMonitorPage.so
/V3/usr/lib64/libPlasmaSystemMonitorTable.so
/usr/lib64/libPlasmaSystemMonitorPage.so
/usr/lib64/libPlasmaSystemMonitorTable.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/page/libPlasmaSystemMonitorPageplugin.so
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/table/libPlasmaSystemMonitorTableplugin.so
/usr/lib64/qt6/qml/org/kde/ksysguard/page/libPlasmaSystemMonitorPageplugin.so
/usr/lib64/qt6/qml/org/kde/ksysguard/table/libPlasmaSystemMonitorTableplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-systemmonitor/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/plasma-systemmonitor/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-systemmonitor/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/plasma-systemmonitor/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-systemmonitor/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-systemmonitor/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-systemmonitor/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/plasma-systemmonitor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-systemmonitor/ce37caa1aac2e9037a7c5648a7519d5bb0970ed3
/usr/share/package-licenses/plasma-systemmonitor/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ksysguard_face_org.kde.ksysguard.applicationstable.lang -f ksysguard_face_org.kde.ksysguard.processtable.lang -f plasma-systemmonitor.lang
%defattr(-,root,root,-)

