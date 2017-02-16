#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF3D322D0EC4582C3 (cgarcia@igalia.com)
#
Name     : webkitgtk
Version  : 2.14.5
Release  : 2
URL      : https://webkitgtk.org/releases/webkitgtk-2.14.5.tar.xz
Source0  : https://webkitgtk.org/releases/webkitgtk-2.14.5.tar.xz
Source99 : https://webkitgtk.org/releases/webkitgtk-2.14.5.tar.xz.asc
Summary  : GTK+ version of the JavaScriptCore engine
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-3.0 GPL-2.0 ICU LGPL-2.0 LGPL-2.1 MIT
Requires: webkitgtk-lib
Requires: webkitgtk-bin
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
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : ruby

%description
Google C++ Testing Framework
============================
http://code.google.com/p/googletest/

%package bin
Summary: bin components for the webkitgtk package.
Group: Binaries

%description bin
bin components for the webkitgtk package.


%package dev
Summary: dev components for the webkitgtk package.
Group: Development
Requires: webkitgtk-lib
Requires: webkitgtk-bin
Provides: webkitgtk-devel

%description dev
dev components for the webkitgtk package.


%package lib
Summary: lib components for the webkitgtk package.
Group: Libraries

%description lib
lib components for the webkitgtk package.


%package locales
Summary: locales components for the webkitgtk package.
Group: Default

%description locales
locales components for the webkitgtk package.


%prep
%setup -q -n webkitgtk-2.14.5

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487237442
unset LD_AS_NEEDED
mkdir clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition -std=gnu++98"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPORT=GTK -DENABLE_GEOLOCATION=off -DENABLE_SPELLCHECK=off -DUSE_LIBHYPHEN=off -DUSE_LD_GOLD=off -DUSE_SYSTEM_MALLOC=on -DENABLE_MINIBROWSER=ON  -DCMAKE_BUILD_TYPE=Release
make VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1487237442
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang WebKit2GTK-4.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/webkit2gtk-4.0/MiniBrowser
/usr/libexec/webkit2gtk-4.0/WebKitDatabaseProcess
/usr/libexec/webkit2gtk-4.0/WebKitNetworkProcess
/usr/libexec/webkit2gtk-4.0/WebKitPluginProcess
/usr/libexec/webkit2gtk-4.0/WebKitPluginProcess2
/usr/libexec/webkit2gtk-4.0/WebKitWebProcess
/usr/libexec/webkit2gtk-4.0/jsc

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
/usr/include/webkitgtk-4.0/webkit2/WebKitAuthenticationRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitAutocleanups.h
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
/usr/include/webkitgtk-4.0/webkit2/WebKitNotification.h
/usr/include/webkitgtk-4.0/webkit2/WebKitNotificationPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPermissionRequest.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPlugin.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPolicyDecision.h
/usr/include/webkitgtk-4.0/webkit2/WebKitPrintOperation.h
/usr/include/webkitgtk-4.0/webkit2/WebKitResponsePolicyDecision.h
/usr/include/webkitgtk-4.0/webkit2/WebKitScriptDialog.h
/usr/include/webkitgtk-4.0/webkit2/WebKitScriptWorld.h
/usr/include/webkitgtk-4.0/webkit2/WebKitSecurityManager.h
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
/usr/include/webkitgtk-4.0/webkit2/WebKitWebResource.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebView.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebViewBase.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebViewSessionState.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWebsiteDataManager.h
/usr/include/webkitgtk-4.0/webkit2/WebKitWindowProperties.h
/usr/include/webkitgtk-4.0/webkit2/webkit-web-extension.h
/usr/include/webkitgtk-4.0/webkit2/webkit2.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMAttr.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMAttrUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMAudioTrack.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMAudioTrackList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMBarProp.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMBatteryManager.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMBlob.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMBlobUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCDATASection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSRule.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSRuleList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSRuleUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSStyleDeclaration.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSStyleSheet.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCSSValue.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCharacterData.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCharacterDataUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMComment.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCustom.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMCustomUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMApplicationCache.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMCSSNamespace.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMImplementation.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMMimeType.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMMimeTypeArray.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMNamedFlowCollection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMPlugin.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMPluginArray.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMSelection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMStringList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMStringMap.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMTokenList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMWindow.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMWindowSpeechSynthesis.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDOMWindowUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDataCue.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDatabase.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDeprecated.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocument.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentFragment.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentFragmentUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentType.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentTypeUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMDocumentUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMEventTarget.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMEventUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMFile.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMFileList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMFileUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMGamepad.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMGamepadList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMGeolocation.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAnchorElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAnchorElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAppletElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAreaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAreaElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLAudioElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBRElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBaseElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLBodyElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLButtonElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLButtonElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLCanvasElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLCollection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDetailsElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDirectoryElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDivElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLDocument.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLEmbedElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFieldSetElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFieldSetElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFontElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFormElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFormElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFrameElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLFrameSetElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHRElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHeadElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHeadingElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHtmlElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLHtmlElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLIFrameElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLIFrameElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLImageElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLImageElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLInputElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLInputElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLKeygenElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLIElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLabelElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLabelElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLegendElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLinkElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLLinkElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMapElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMarqueeElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMarqueeElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMediaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMenuElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLMetaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLModElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOListElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLObjectElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLObjectElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptGroupElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptionsCollection.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLOptionsCollectionUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLParagraphElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLParamElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLPreElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLQuoteElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLScriptElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLScriptElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLSelectElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLSelectElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLStyleElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLStyleElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableCaptionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableCellElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableColElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableRowElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTableSectionElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTextAreaElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTextAreaElementUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLTitleElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLUListElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHTMLVideoElement.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMHistory.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMKeyboardEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMLocation.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaController.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaDevices.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaError.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaQueryList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMediaTrackSupportedConstraints.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMessagePort.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMouseEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMMouseEventUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNamedNodeMap.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNavigator.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNavigatorMediaDevices.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNode.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeFilter.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeIterator.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMNodeUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMObject.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMPerformance.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMPerformanceEntry.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMPerformanceNavigation.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMPerformanceTiming.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMProcessingInstruction.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMRange.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMRangeUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMScreen.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMSpeechSynthesis.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMSpeechSynthesisEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMSpeechSynthesisUtterance.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMSpeechSynthesisVoice.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStorage.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStorageInfo.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStorageQuota.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStyleMedia.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStyleSheet.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMStyleSheetList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMText.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTextTrack.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTextTrackCue.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTextTrackCueList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTextTrackList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTimeRanges.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTouch.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTrackEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMTreeWalker.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMUIEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMUIEventUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMUserMessageHandler.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMUserMessageHandlersNamespace.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMVTTCue.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMValidityState.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMVideoPlaybackQuality.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMVideoTrack.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMVideoTrackList.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWebKitNamedFlow.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWebKitNamespace.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWebKitPoint.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWheelEvent.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMWheelEventUnstable.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathExpression.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathNSResolver.h
/usr/include/webkitgtk-4.0/webkitdom/WebKitDOMXPathResult.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdom.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomautocleanups-unstable.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomautocleanups.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomdefines-unstable.h
/usr/include/webkitgtk-4.0/webkitdom/webkitdomdefines.h
/usr/lib64/girepository-1.0/JavaScriptCore-4.0.typelib
/usr/lib64/girepository-1.0/WebKit2-4.0.typelib
/usr/lib64/girepository-1.0/WebKit2WebExtension-4.0.typelib
/usr/lib64/libjavascriptcoregtk-4.0.so
/usr/lib64/libwebkit2gtk-4.0.so
/usr/lib64/pkgconfig/javascriptcoregtk-4.0.pc
/usr/lib64/pkgconfig/webkit2gtk-4.0.pc
/usr/lib64/pkgconfig/webkit2gtk-web-extension-4.0.pc
/usr/share/gir-1.0/*.gir

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjavascriptcoregtk-4.0.so.18
/usr/lib64/libjavascriptcoregtk-4.0.so.18.4.12
/usr/lib64/libwebkit2gtk-4.0.so.37
/usr/lib64/libwebkit2gtk-4.0.so.37.14.12
/usr/lib64/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files locales -f WebKit2GTK-4.0.lang
%defattr(-,root,root,-)

