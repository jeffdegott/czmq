################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from . import utils
from . import destructors
libczmq_destructors = destructors.lib

class Zconfig(object):
    """
    work with config files written in rfc.zeromq.org/spec:4/ZPL.
    """

    def __init__(self, name, parent):
        """
        Create new config item
        """
        p = utils.lib.zconfig_new(utils.to_bytes(name), parent._p)
        if p == utils.ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = utils.ffi.gc(p, libczmq_destructors.zconfig_destroy_py)

    @staticmethod
    def load(filename):
        """
        Load a config tree from a specified ZPL text file; returns a zconfig_t
        reference for the root, if the file exists and is readable. Returns NULL
        if the file does not exist.
        """
        return utils.lib.zconfig_load(utils.to_bytes(filename))

    @staticmethod
    def loadf(format, *format_args):
        """
        Equivalent to zconfig_load, taking a format string instead of a fixed
        filename.
        """
        return utils.lib.zconfig_loadf(format, *format_args)

    def dup(self):
        """
        Create copy of zconfig, caller MUST free the value
        Create copy of config, as new zconfig object. Returns a fresh zconfig_t
        object. If config is null, or memory was exhausted, returns null.
        """
        return utils.lib.zconfig_dup(self._p)

    def name(self):
        """
        Return name of config item
        """
        return utils.lib.zconfig_name(self._p)

    def value(self):
        """
        Return value of config item
        """
        return utils.lib.zconfig_value(self._p)

    def put(self, path, value):
        """
        Insert or update configuration key with value
        """
        utils.lib.zconfig_put(self._p, utils.to_bytes(path), utils.to_bytes(value))

    def putf(self, path, format, *format_args):
        """
        Equivalent to zconfig_put, accepting a format specifier and variable
        argument list, instead of a single string value.
        """
        utils.lib.zconfig_putf(self._p, utils.to_bytes(path), format, *format_args)

    def get(self, path, default_value):
        """
        Get value for config item into a string value; leading slash is optional
        and ignored.
        """
        return utils.lib.zconfig_get(self._p, utils.to_bytes(path), utils.to_bytes(default_value))

    def set_name(self, name):
        """
        Set config item name, name may be NULL
        """
        utils.lib.zconfig_set_name(self._p, utils.to_bytes(name))

    def set_value(self, format, *format_args):
        """
        Set new value for config item. The new value may be a string, a printf
        format, or NULL. Note that if string may possibly contain '%', or if it
        comes from an insecure source, you must use '%s' as the format, followed
        by the string.
        """
        utils.lib.zconfig_set_value(self._p, format, *format_args)

    def child(self):
        """
        Find our first child, if any
        """
        return utils.lib.zconfig_child(self._p)

    def next(self):
        """
        Find our first sibling, if any
        """
        return utils.lib.zconfig_next(self._p)

    def locate(self, path):
        """
        Find a config item along a path; leading slash is optional and ignored.
        """
        return utils.lib.zconfig_locate(self._p, utils.to_bytes(path))

    def at_depth(self, level):
        """
        Locate the last config item at a specified depth
        """
        return utils.lib.zconfig_at_depth(self._p, level)

    def execute(self, handler, arg):
        """
        Execute a callback for each config item in the tree; returns zero if
        successful, else -1.
        """
        return utils.lib.zconfig_execute(self._p, handler, arg._p)

    def set_comment(self, format, *format_args):
        """
        Add comment to config item before saving to disk. You can add as many
        comment lines as you like. If you use a null format, all comments are
        deleted.
        """
        utils.lib.zconfig_set_comment(self._p, format, *format_args)

    def comments(self):
        """
        Return comments of config item, as zlist.
        """
        return utils.lib.zconfig_comments(self._p)

    def save(self, filename):
        """
        Save a config tree to a specified ZPL text file, where a filename
        "-" means dump to standard output.
        """
        return utils.lib.zconfig_save(self._p, utils.to_bytes(filename))

    def savef(self, format, *format_args):
        """
        Equivalent to zconfig_save, taking a format string instead of a fixed
        filename.
        """
        return utils.lib.zconfig_savef(self._p, format, *format_args)

    def filename(self):
        """
        Report filename used during zconfig_load, or NULL if none
        """
        return utils.lib.zconfig_filename(self._p)

    @staticmethod
    def reload(self_p):
        """
        Reload config tree from same file that it was previously loaded from.
        Returns 0 if OK, -1 if there was an error (and then does not change
        existing data).
        """
        return utils.lib.zconfig_reload(utils.ffi.new("zconfig_t **", self_p._p))

    @staticmethod
    def chunk_load(chunk):
        """
        Load a config tree from a memory chunk
        """
        return utils.lib.zconfig_chunk_load(chunk._p)

    def chunk_save(self):
        """
        Save a config tree to a new memory chunk
        """
        return utils.lib.zconfig_chunk_save(self._p)

    @staticmethod
    def str_load(string):
        """
        Load a config tree from a null-terminated string
        """
        return utils.lib.zconfig_str_load(utils.to_bytes(string))

    def str_save(self):
        """
        Save a config tree to a new null terminated string
        """
        return utils.lib.zconfig_str_save(self._p)

    def has_changed(self):
        """
        Return true if a configuration tree was loaded from a file and that
        file has changed in since the tree was loaded.
        """
        return utils.lib.zconfig_has_changed(self._p)

    def remove_subtree(self):
        """
        Destroy subtree (all children)
        """
        utils.lib.zconfig_remove_subtree(self._p)

    @staticmethod
    def remove(self_p):
        """
        Destroy node and subtree (all children)
        """
        utils.lib.zconfig_remove(utils.ffi.new("zconfig_t **", self_p._p))

    def fprint(self, file):
        """
        Print the config file to open stream
        """
        utils.lib.zconfig_fprint(self._p, file)

    def print_py(self):
        """
        Print properties of object
        """
        utils.lib.zconfig_print(self._p)

    @staticmethod
    def test(verbose):
        """
        Self test of this class
        """
        utils.lib.zconfig_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################