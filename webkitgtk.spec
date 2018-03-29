#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF3D322D0EC4582C3 (cgarcia@igalia.com)
#
Name     : webkitgtk
Version  : 2.20.0
Release  : 24
URL      : https://webkitgtk.org/releases/webkitgtk-2.20.0.tar.xz
Source0  : https://webkitgtk.org/releases/webkitgtk-2.20.0.tar.xz
Source99 : https://webkitgtk.org/releases/webkitgtk-2.20.0.tar.xz.asc
Summary  : GTK+ version of the JavaScriptCore engine
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause ICU LGPL-2.0 LGPL-2.1 MIT
Requires: webkitgtk-bin
Requires: webkitgtk-data
Requires: webkitgtk-lib
Requires: webkitgtk-locales
BuildRequires : bison
BuildRequires : cmake
BuildRequires : flex
BuildRequires : fontconfig-dev
BuildRequires : freetype-dev
BuildRequires : gjs-dev
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : harfbuzz-dev
BuildRequires : icu4c-dev
BuildRequires : libXcomposite-dev
BuildRequires : libc-bin
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libnotify-dev
BuildRequires : libpng-dev
BuildRequires : libsoup-dev
BuildRequires : libwebp-dev
BuildRequires : libxslt-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libwoff2dec)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : ruby
Patch1: utf.patch

%description
Google C++ Testing Framework
============================
http://code.google.com/p/googletest/

%package bin
Summary: bin components for the webkitgtk package.
Group: Binaries
Requires: webkitgtk-data

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
Requires: webkitgtk-lib
Requires: webkitgtk-bin
Requires: webkitgtk-data
Provides: webkitgtk-devel

%description dev
dev components for the webkitgtk package.


%package lib
Summary: lib components for the webkitgtk package.
Group: Libraries
Requires: webkitgtk-data

%description lib
lib components for the webkitgtk package.


%package locales
Summary: locales components for the webkitgtk package.
Group: Default

%description locales
locales components for the webkitgtk package.


%prep
%setup -q -n webkitgtk-2.20.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522336443
unset LD_AS_NEEDED
mkdir clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -std=gnu++98"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPORT=GTK -DENABLE_GEOLOCATION=off -DENABLE_SPELLCHECK=off -DUSE_LIBHYPHEN=off -DUSE_LD_GOLD=off -DUSE_SYSTEM_MALLOC=on -DENABLE_MINIBROWSER=ON  -DCMAKE_BUILD_TYPE=Release -DUSE_GSTREAMER_GL=OFF -DPYTHON=/usr/bin/python2
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1522336443
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang WebKit2GTK-4.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/WebKitWebDriver
/usr/libexec/webkit2gtk-4.0/MiniBrowser
/usr/libexec/webkit2gtk-4.0/WebKitNetworkProcess
/usr/libexec/webkit2gtk-4.0/WebKitPluginProcess
/usr/libexec/webkit2gtk-4.0/WebKitPluginProcess2
/usr/libexec/webkit2gtk-4.0/WebKitStorageProcess
/usr/libexec/webkit2gtk-4.0/WebKitWebProcess
/usr/libexec/webkit2gtk-4.0/jsc

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
/usr/include/webkitgtk-4.0/webkit2/WebKitGeolocationPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitHitTestResult.h
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
/usr/include/webkitgtk-4.0/webkit2/WebKitUserContent.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserContentManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitUserMediaPermissionRequest.h
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
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsiteDataManager.h
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
/usr/lib64/libjavascriptcoregtk-4.0.so.18.7.8
/usr/lib64/libwebkit2gtk-4.0.so.37
/usr/lib64/libwebkit2gtk-4.0.so.37.28.0
/usr/lib64/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files locales -f WebKit2GTK-4.0.lang
%defattr(-,root,root,-)

