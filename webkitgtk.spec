#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF3D322D0EC4582C3 (cgarcia@igalia.com)
#
Name     : webkitgtk
Version  : 2.30.5
Release  : 68
URL      : https://webkitgtk.org/releases/webkitgtk-2.30.5.tar.xz
Source0  : https://webkitgtk.org/releases/webkitgtk-2.30.5.tar.xz
Source1  : https://webkitgtk.org/releases/webkitgtk-2.30.5.tar.xz.asc
Summary  : Web content engine for GTK - web process extensions
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT Unicode-DFS-2016
Requires: webkitgtk-bin = %{version}-%{release}
Requires: webkitgtk-data = %{version}-%{release}
Requires: webkitgtk-lib = %{version}-%{release}
Requires: webkitgtk-libexec = %{version}-%{release}
Requires: webkitgtk-license = %{version}-%{release}
Requires: webkitgtk-locales = %{version}-%{release}
Requires: bubblewrap
Requires: xdg-dbus-proxy
BuildRequires : bison
BuildRequires : bubblewrap
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : extra-cmake-modules gperf
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : flex
BuildRequires : fontconfig-dev
BuildRequires : freetype-dev
BuildRequires : gjs-dev
BuildRequires : glibc-dev
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : harfbuzz-dev
BuildRequires : icu4c-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libXcomposite-dev
BuildRequires : libc-bin
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libnotify-dev
BuildRequires : libpng-dev
BuildRequires : libsoup-dev
BuildRequires : libwebp-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : mesa-dev
BuildRequires : nghttp2-dev
BuildRequires : openjpeg
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(atk-bridge-2.0)
BuildRequires : pkgconfig(atspi-2)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gl)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(harfbuzz-icu)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpsl)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtasn1)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwoff2common)
BuildRequires : pkgconfig(libwoff2dec)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xt)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : xdg-dbus-proxy
BuildRequires : zlib-dev

%description
This module is a simple module that parses the proposed MIME spec listed
at http://freedesktop.org/.  It is currently targeted at version 0.12.
There are no formal releases planned for this module, and it is not
intended to be installed at this time.  Rather, it is meant to be used
by other libraries or applications to add support for the MIME system.

%package bin
Summary: bin components for the webkitgtk package.
Group: Binaries
Requires: webkitgtk-data = %{version}-%{release}
Requires: webkitgtk-libexec = %{version}-%{release}
Requires: webkitgtk-license = %{version}-%{release}

%description bin
bin components for the webkitgtk package.


%package data
Summary: data components for the webkitgtk package.
Group: Data

%description data
data components for the webkitgtk package.


%package dev
Summary: dev components for the webkitgtk package.
Group: Development
Requires: webkitgtk-lib = %{version}-%{release}
Requires: webkitgtk-bin = %{version}-%{release}
Requires: webkitgtk-data = %{version}-%{release}
Provides: webkitgtk-devel = %{version}-%{release}
Requires: webkitgtk = %{version}-%{release}

%description dev
dev components for the webkitgtk package.


%package lib
Summary: lib components for the webkitgtk package.
Group: Libraries
Requires: webkitgtk-data = %{version}-%{release}
Requires: webkitgtk-libexec = %{version}-%{release}
Requires: webkitgtk-license = %{version}-%{release}

%description lib
lib components for the webkitgtk package.


%package libexec
Summary: libexec components for the webkitgtk package.
Group: Default
Requires: webkitgtk-license = %{version}-%{release}

%description libexec
libexec components for the webkitgtk package.


%package license
Summary: license components for the webkitgtk package.
Group: Default

%description license
license components for the webkitgtk package.


%package locales
Summary: locales components for the webkitgtk package.
Group: Default

%description locales
locales components for the webkitgtk package.


%prep
%setup -q -n webkitgtk-2.30.5
cd %{_builddir}/webkitgtk-2.30.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613179009
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -std=gnu++98"
%cmake .. -DPORT=GTK \
-DENABLE_GEOLOCATION=off \
-DENABLE_SPELLCHECK=off \
-DUSE_LIBHYPHEN=off \
-DUSE_LD_GOLD=off \
-DUSE_SYSTEM_MALLOC=on \
-DENABLE_MINIBROWSER=ON \
-DCMAKE_BUILD_TYPE=Release \
-DUSE_GSTREAMER_GL=OFF \
-DPYTHON=/usr/bin/python2 \
-DUSE_OPENJPEG=off \
-DUSE_WPE_RENDERER=off
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1613179009
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/webkitgtk
cp %{_builddir}/webkitgtk-2.30.5/Source/JavaScriptCore/COPYING.LIB %{buildroot}/usr/share/package-licenses/webkitgtk/130f5281a2ef2a49822787e013323bde2ff119dd
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/37126a0eda0b30f44070f59e6833187e99a7eb83
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/common/third_party/smhasher/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/819e6935c5ac3ae7bcb7470cb81c07cc383e80eb
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/common/third_party/xxhash/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/390f8904578d05817ab7cafe1f470cd283bcfe93
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/libANGLE/renderer/vulkan/shaders/src/third_party/ffx_spd/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/18f2c8a1b68673441f7ae71085ce98b7cad01734
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/tests/test_utils/third_party/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/5ebf8574fea54a1c549c090652f327376b1376aa
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/third_party/compiler/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/dbb4b3a7c493484294639613ed59f1f5e7f94ada
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/665f7371da2b70dc3908c7c1e8b43bbbada8e4c3
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/src/third_party/volk/LICENSE.md %{buildroot}/usr/share/package-licenses/webkitgtk/f12c9d338be92bacfa1e21c513e3517ad3190931
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/tools/flex-bison/third_party/m4sugar/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/tools/flex-bison/third_party/skeletons/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/ANGLE/util/windows/third_party/StackWalker/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/33fe6f9feb6fc711ff8b5dc59283453f84fcbfe3
cp %{_builddir}/webkitgtk-2.30.5/Source/ThirdParty/gtest/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/webkitgtk-2.30.5/Source/WTF/icu/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/a3c672a8f8677817b488d042bd4fc597d7785285
cp %{_builddir}/webkitgtk-2.30.5/Source/WTF/wtf/dtoa/COPYING %{buildroot}/usr/share/package-licenses/webkitgtk/8d434c9c1704b544a8b0652efbc323380b67f9bc
cp %{_builddir}/webkitgtk-2.30.5/Source/WTF/wtf/dtoa/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/8d434c9c1704b544a8b0652efbc323380b67f9bc
cp %{_builddir}/webkitgtk-2.30.5/Source/WebCore/LICENSE-APPLE %{buildroot}/usr/share/package-licenses/webkitgtk/7ea0ac726dfef36527dfe261d1f2ae28c8f96d4d
cp %{_builddir}/webkitgtk-2.30.5/Source/WebCore/LICENSE-LGPL-2 %{buildroot}/usr/share/package-licenses/webkitgtk/31c49697af1092e3e9e230f93c0e0f7dd9694abb
cp %{_builddir}/webkitgtk-2.30.5/Source/WebCore/LICENSE-LGPL-2.1 %{buildroot}/usr/share/package-licenses/webkitgtk/1a180647a31404e0cf993fa333cdb7f7e75eaba5
cp %{_builddir}/webkitgtk-2.30.5/Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/e7ada8ae78ebdb41cc7c8e9dbad43c5870412bd7
cp %{_builddir}/webkitgtk-2.30.5/Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/26dd70b52c7c7111ca8913fc0bc240dc28ca15c0
cp %{_builddir}/webkitgtk-2.30.5/Source/WebInspectorUI/UserInterface/External/three.js/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk/eb5e50200f181f35271557d301ffd7784df64f79
pushd clr-build
%make_install
popd
%find_lang WebKit2GTK-4.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/WebKitWebDriver

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/JavaScriptCore-4.0.typelib
/usr/lib64/girepository-1.0/WebKit2-4.0.typelib
/usr/lib64/girepository-1.0/WebKit2WebExtension-4.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/webkitgtk-4.0/JavaScriptCore/JSBase.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JSContextRef.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JSObjectRef.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JSStringRef.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JSTypedArray.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JSValueRef.h
/usr/include/webkitgtk-4.0/JavaScriptCore/JavaScript.h
/usr/include/webkitgtk-4.0/JavaScriptCore/WebKitAvailability.h
/usr/include/webkitgtk-4.0/jsc/JSCAutocleanups.h
/usr/include/webkitgtk-4.0/jsc/JSCClass.h
/usr/include/webkitgtk-4.0/jsc/JSCContext.h
/usr/include/webkitgtk-4.0/jsc/JSCDefines.h
/usr/include/webkitgtk-4.0/jsc/JSCException.h
/usr/include/webkitgtk-4.0/jsc/JSCOptions.h
/usr/include/webkitgtk-4.0/jsc/JSCValue.h
/usr/include/webkitgtk-4.0/jsc/JSCVersion.h
/usr/include/webkitgtk-4.0/jsc/JSCVirtualMachine.h
/usr/include/webkitgtk-4.0/jsc/JSCWeakValue.h
/usr/include/webkitgtk-4.0/jsc/jsc.h
/usr/include/webkitgtk-4.0/webkit2/WebKitApplicationInfo.h
/usr/include/webkitgtk-4.0/webkit2/WebKitAuthenticationRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitAutocleanups.h
/usr/include/webkitgtk-4.0/webkit2/WebKitAutomationSession.h
/usr/include/webkitgtk-4.0/webkit2/WebKitBackForwardList.h
/usr/include/webkitgtk-4.0/webkit2/WebKitBackForwardListItem.h
/usr/include/webkitgtk-4.0/webkit2/WebKitColorChooserRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitConsoleMessage.h
/usr/include/webkitgtk-4.0/webkit2/WebKitContextMenu.h
/usr/include/webkitgtk-4.0/webkit2/WebKitContextMenuActions.h
/usr/include/webkitgtk-4.0/webkit2/WebKitContextMenuItem.h
/usr/include/webkitgtk-4.0/webkit2/WebKitCookieManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitCredential.h
/usr/include/webkitgtk-4.0/webkit2/WebKitDefines.h
/usr/include/webkitgtk-4.0/webkit2/WebKitDeviceInfoPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitDownload.h
/usr/include/webkitgtk-4.0/webkit2/WebKitEditingCommands.h
/usr/include/webkitgtk-4.0/webkit2/WebKitEditorState.h
/usr/include/webkitgtk-4.0/webkit2/WebKitEnumTypes.h
/usr/include/webkitgtk-4.0/webkit2/WebKitError.h
/usr/include/webkitgtk-4.0/webkit2/WebKitFaviconDatabase.h
/usr/include/webkitgtk-4.0/webkit2/WebKitFileChooserRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitFindController.h
/usr/include/webkitgtk-4.0/webkit2/WebKitFormSubmissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitForwardDeclarations.h
/usr/include/webkitgtk-4.0/webkit2/WebKitFrame.h
/usr/include/webkitgtk-4.0/webkit2/WebKitGeolocationManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitGeolocationPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitHitTestResult.h
/usr/include/webkitgtk-4.0/webkit2/WebKitInputMethodContext.h
/usr/include/webkitgtk-4.0/webkit2/WebKitInstallMissingMediaPluginsPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitJavascriptResult.h
/usr/include/webkitgtk-4.0/webkit2/WebKitMimeInfo.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNavigationAction.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNavigationPolicyDecision.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNetworkProxySettings.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNotification.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNotificationPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitOptionMenu.h
/usr/include/webkitgtk-4.0/webkit2/WebKitOptionMenuItem.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPlugin.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPointerLockPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPolicyDecision.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPrintCustomWidget.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPrintOperation.h
/usr/include/webkitgtk-4.0/webkit2/WebKitResponsePolicyDecision.h
/usr/include/webkitgtk-4.0/webkit2/WebKitScriptDialog.h
/usr/include/webkitgtk-4.0/webkit2/WebKitScriptWorld.h
/usr/include/webkitgtk-4.0/webkit2/WebKitSecurityManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitSecurityOrigin.h
/usr/include/webkitgtk-4.0/webkit2/WebKitSettings.h
/usr/include/webkitgtk-4.0/webkit2/WebKitURIRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitURIResponse.h
/usr/include/webkitgtk-4.0/webkit2/WebKitURISchemeRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitURIUtilities.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserContent.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserContentFilterStore.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserContentManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserMediaPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserMessage.h
/usr/include/webkitgtk-4.0/webkit2/WebKitVersion.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebContext.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebEditor.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebExtension.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebExtensionAutocleanups.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebHitTestResult.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebInspector.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebPage.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebProcessEnumTypes.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebResource.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebView.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebViewBase.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebViewSessionState.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsiteData.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsiteDataAccessPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsiteDataManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsitePolicies.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWindowProperties.h
/usr/include/webkitgtk-4.0/webkit2/webkit-web-extension.h
/usr/include/webkitgtk-4.0/webkit2/webkit2.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMAttr.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMBlob.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCDATASection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSRule.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSRuleList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSStyleDeclaration.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSStyleSheet.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSValue.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCharacterData.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMClientRect.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMClientRectList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMComment.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCustom.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCustomUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMImplementation.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMSelection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMTokenList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMWindow.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMWindowUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDeprecated.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocument.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentFragment.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentFragmentUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentType.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMEventTarget.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMFile.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMFileList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAnchorElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAppletElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAreaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBRElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBaseElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBodyElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLButtonElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLCanvasElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLCollection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDirectoryElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDivElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDocument.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLEmbedElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFieldSetElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFontElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFormElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFrameElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFrameSetElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHRElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHeadElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHeadingElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHtmlElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLIFrameElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLImageElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLInputElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLIElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLabelElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLegendElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLinkElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMapElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMarqueeElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMenuElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMetaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLModElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLObjectElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptGroupElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptionsCollection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLParagraphElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLParamElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLPreElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLQuoteElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLScriptElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLSelectElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLStyleElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableCaptionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableCellElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableColElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableRowElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableSectionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTextAreaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTitleElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLUListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMKeyboardEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMouseEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNamedNodeMap.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNode.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeFilter.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeIterator.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMObject.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMProcessingInstruction.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMRange.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMRangeUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStyleSheet.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStyleSheetList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMText.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTreeWalker.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMUIEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWheelEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathExpression.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathNSResolver.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathResult.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdom.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomautocleanups.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomdefines.h
/usr/lib64/libjavascriptcoregtk-4.0.so
/usr/lib64/libwebkit2gtk-4.0.so
/usr/lib64/pkgconfig/javascriptcoregtk-4.0.pc
/usr/lib64/pkgconfig/webkit2gtk-4.0.pc
/usr/lib64/pkgconfig/webkit2gtk-web-extension-4.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjavascriptcoregtk-4.0.so.18
/usr/lib64/libjavascriptcoregtk-4.0.so.18.17.13
/usr/lib64/libwebkit2gtk-4.0.so.37
/usr/lib64/libwebkit2gtk-4.0.so.37.49.9
/usr/lib64/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/webkit2gtk-4.0/MiniBrowser
/usr/libexec/webkit2gtk-4.0/WebKitNetworkProcess
/usr/libexec/webkit2gtk-4.0/WebKitPluginProcess
/usr/libexec/webkit2gtk-4.0/WebKitWebProcess
/usr/libexec/webkit2gtk-4.0/jsc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/webkitgtk/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/webkitgtk/130f5281a2ef2a49822787e013323bde2ff119dd
/usr/share/package-licenses/webkitgtk/18f2c8a1b68673441f7ae71085ce98b7cad01734
/usr/share/package-licenses/webkitgtk/1a180647a31404e0cf993fa333cdb7f7e75eaba5
/usr/share/package-licenses/webkitgtk/26dd70b52c7c7111ca8913fc0bc240dc28ca15c0
/usr/share/package-licenses/webkitgtk/31c49697af1092e3e9e230f93c0e0f7dd9694abb
/usr/share/package-licenses/webkitgtk/33fe6f9feb6fc711ff8b5dc59283453f84fcbfe3
/usr/share/package-licenses/webkitgtk/37126a0eda0b30f44070f59e6833187e99a7eb83
/usr/share/package-licenses/webkitgtk/390f8904578d05817ab7cafe1f470cd283bcfe93
/usr/share/package-licenses/webkitgtk/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/webkitgtk/5ebf8574fea54a1c549c090652f327376b1376aa
/usr/share/package-licenses/webkitgtk/665f7371da2b70dc3908c7c1e8b43bbbada8e4c3
/usr/share/package-licenses/webkitgtk/7ea0ac726dfef36527dfe261d1f2ae28c8f96d4d
/usr/share/package-licenses/webkitgtk/819e6935c5ac3ae7bcb7470cb81c07cc383e80eb
/usr/share/package-licenses/webkitgtk/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/webkitgtk/8d434c9c1704b544a8b0652efbc323380b67f9bc
/usr/share/package-licenses/webkitgtk/a3c672a8f8677817b488d042bd4fc597d7785285
/usr/share/package-licenses/webkitgtk/dbb4b3a7c493484294639613ed59f1f5e7f94ada
/usr/share/package-licenses/webkitgtk/e7ada8ae78ebdb41cc7c8e9dbad43c5870412bd7
/usr/share/package-licenses/webkitgtk/eb5e50200f181f35271557d301ffd7784df64f79
/usr/share/package-licenses/webkitgtk/f12c9d338be92bacfa1e21c513e3517ad3190931

%files locales -f WebKit2GTK-4.0.lang
%defattr(-,root,root,-)

