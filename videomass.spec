%define oname %(n=%{name}; echo ${n^})

Summary:	Cross-platform GUI for FFmpeg and yt-dlp
Name:		videomass
Version:	5.0.20
Release:	1
License:	GPLv3+
Group:		Video
Url:		https://github.com/jeanslack/Videomass
Source0:	https://github.com/jeanslack/Videomass/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pypubsub)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(wxpython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
#BuildRequires:	ffmpeg

Requires:	python3
Requires:	python%{pyver}dist(wxpython)

Recommends:	ffmpeg
Recommends:	yt-dlp
Recommends:	youtube-dl

BuildArch:	noarch


%description
Videomass is a powerful, multitasking and cross-platform graphical user
 interface (GUI) for FFmpeg and yt-dlp.
 .
 It offers a wide range of features and functions, making it a comprehensive
 software solution.
 .
 Videomass is written in Python3 using the wxPython-Phoenix GUI toolkit

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.*-info/
%{_datadir}/applications/io.github.jeanslack.%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_iconsdir}/hicolor/*/apps/%{name}.xpm
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/io.github.jeanslack.%{name}.appdata.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py_install

# locales
%find_lang %{name} --all-name

