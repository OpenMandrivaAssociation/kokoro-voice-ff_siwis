Name:		kokoro-voice-ff_siwis
Version:	1.0
Release:	1
Summary:	French female Kokoro voice ff_siwis
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-fr
Provides:	kokoro-voice-fr_FR
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/ff_siwis.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m ff_siwis

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/ff_siwis.pt

%files
%{_datadir}/kokoro/voices/ff_siwis.pt
