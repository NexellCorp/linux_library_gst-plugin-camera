Name:    gst-plugins-camera-s5p6818
Version: 0.0.1
Release: 0
License: Apache 2.0
Summary: gstreamer plugin camera
Group: Development/Libraries
Source:  %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	gstreamer1-devel
BuildRequires:	glibc-devel
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:	gst-plugins-renderer-devel
BuildRequires:	nx-drm-allocator-devel
BuildRequires:	nx-v4l2-devel

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
gstreamer plugin camera

%package devel
Summary: gstreamer plugin camera
Group: Development/Libraries
License: Apache 2.0
Requires: %{name} = %{version}-%{release}

%description devel
gstreamer plugin camera (devel)

%prep
%setup -q

%build
make

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib/gstreamer-1.0
cp %{_builddir}/%{name}-%{version}/libgstnxcamerasrc.so  %{buildroot}/usr/lib/gstreamer-1.0

%files
%attr (0644, root, root) %{_libdir}/gstreamer-1.0/libgstnxcamerasrc.so
