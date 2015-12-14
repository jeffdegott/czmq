#!/bin/bash
# copy me in czmq/bindings/jni/buidlme.sh and make me executable with chmod +x
source android_build_helper.sh
android_build_env

rm -Rf build
mkdir build
cd build
cmake -v -DCMAKE_TOOLCHAIN_FILE=../android_toolchain.cmake ..
ln -s $ANDROID_NDK_ROOT/platforms/android-8/arch-arm/usr/lib/crtend_so.o
ln -s $ANDROID_NDK_ROOT/platforms/android-8/arch-arm/usr/lib/crtbegin_so.o
make
