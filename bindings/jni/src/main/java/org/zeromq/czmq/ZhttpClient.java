/*
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
*/
package org.zeromq.czmq;

import org.scijava.nativelib.NativeLoader;

public class ZhttpClient implements AutoCloseable{
    static {
        if (System.getProperty("java.vm.vendor").contains("Android")) {
            System.loadLibrary("czmqjni");
        } else {
            try {
                NativeLoader.loadLibrary("czmqjni");
            } catch (Exception e) {
                System.exit (-1);
            }
        }
    }
    public long self;
    /*
    Create a new http client
    */
    native static long __new (boolean verbose);
    public ZhttpClient (boolean verbose) {
        /*  TODO: if __new fails, self is null...            */
        self = __new (verbose);
    }
    public ZhttpClient (long pointer) {
        self = pointer;
    }
    /*
    Destroy an http client
    */
    native static void __destroy (long self);
    @Override
    public void close () {
        __destroy (self);
        self = 0;
    }
    /*
    Send a get request to the url, headers is optional.
    Use userp to identify response when making multiple requests simultaneously.
    */
    native static int __get (long self, String url, long headers, long userp);
    public int get (String url, Zlistx headers, long userp) {
        return __get (self, url, headers.self, userp);
    }
    /*
    Receive the response for one of the requests. Blocks until a response is ready.
    Use userp to identify the request.
    */
    native static int __recv (long self, int responseCode, long data, long userp);
    public int recv (int responseCode, Zchunk data, long userp) {
        return __recv (self, responseCode, data.self, userp);
    }
    /*
    Self test of this class.
    */
    native static void __test (boolean verbose);
    public static void test (boolean verbose) {
        __test (verbose);
    }
}
