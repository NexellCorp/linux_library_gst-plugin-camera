ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

AM_CFLAGS = \
	$(WARN_CFLAGS) \
	-I${includedir} \
	-I./ \
	-I${GST_PATH}/staging/usr/include \
	-I${GST_PATH}/staging/usr/lib/glib-2.0/include \
	-I${GST_PATH}/staging/usr/include/glib-2.0 \
	-I${GST_PATH}/staging/usr/include/gstreamer-1.0

libgstnxcamerasrc_la_LTLIBRARIES = libgstnxcamerasrc.la
libgstnxcamerasrc_ladir = ${libdir}
libgstnxcamerasrc_la_LDFLAGS = -L${libdir} -L${GST_PATH}/target/usr/lib 
libgstnxcamerasrc_la_LIBADD = -lnx_drm_allocator -lnx_v4l2 -lgstallocators-1.0 -lgstbase-1.0 -lgmodule-2.0 -lgobject-2.0 -lglib-2.0
libgstnxcamerasrc_la_SOURCES = \
	gstcamerasrc.c

gstnxcamerasrcincludedir = ${includedir}
gstnxcamerasrcinclude_HEADERS = \
	gstcamerasrc.h


