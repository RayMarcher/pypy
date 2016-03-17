class AppTestUserObject:
    def test_dictproxy(self):
        class NotEmpty(object):
            a = 1
        NotEmpty.a = 1
        NotEmpty.a = 1
        NotEmpty.a = 1
        NotEmpty.a = 1
        assert 'a' in NotEmpty.__dict__
        assert 'a' in NotEmpty.__dict__.keys()
        assert 'b' not in NotEmpty.__dict__
        NotEmpty.__dict__['b'] = 4
        assert NotEmpty.b == 4
        del NotEmpty.__dict__['b']
        assert NotEmpty.__dict__.get("b") is None
        raises(TypeError, 'NotEmpty.__dict__[15] = "y"')
        raises(KeyError, 'del NotEmpty.__dict__[15]')

        assert NotEmpty.__dict__.setdefault("string", 1) == 1
        assert NotEmpty.__dict__.setdefault("string", 2) == 1
        assert NotEmpty.string == 1
        raises(TypeError, 'NotEmpty.__dict__.setdefault(15, 1)')

    def test_dictproxy_popitem(self):
        class A(object):
            a = 42
        seen = 0
        try:
            while True:
                key, value = A.__dict__.popitem()
                if key == 'a':
                    assert value == 42
                    seen += 1
        except KeyError:
            pass
        assert seen == 1

    def test_dictproxy_getitem(self):
        class NotEmpty(object):
            a = 1
        assert 'a' in NotEmpty.__dict__
        class substr(str): pass
        assert substr('a') in NotEmpty.__dict__
        # the following are only for py2
        ## assert u'a' in NotEmpty.__dict__
        ## assert NotEmpty.__dict__[u'a'] == 1
        ## assert u'\xe9' not in NotEmpty.__dict__

    def test_dictproxyeq(self):
        class a(object):
            pass
        class b(a):
            stuff = 42
        class c(a):
            stuff = 42
        assert a.__dict__ == a.__dict__
        assert a.__dict__ != b.__dict__
        assert a.__dict__ != {'123': '456'}
        assert {'123': '456'} != a.__dict__
        b.__dict__.pop('__qualname__')
        c.__dict__.pop('__qualname__')
        assert b.__dict__ == c.__dict__

    def test_str_repr(self):
        class a(object):
            pass
        s1 = repr(a.__dict__)
        s2 = str(a.__dict__)
        assert s1 == s2
        assert s1.startswith('mappingproxy({') and s1.endswith('})')

    def test_immutable_dict_on_builtin_type(self):
        raises(TypeError, "int.__dict__['a'] = 1")
        raises((AttributeError, TypeError), "int.__dict__.popitem()")
        raises((AttributeError, TypeError), "int.__dict__.clear()")

    def test_mappingproxy(self):
        dictproxy = type(int.__dict__)
        assert dictproxy is not dict
        assert dictproxy.__name__ == 'mappingproxy'
        raises(TypeError, dictproxy)
        mapping = dict(a=1, b=2, c=3)
        proxy = dictproxy(mapping)
        assert proxy['a'] == 1
        assert 'a' in proxy
        assert 'z' not in proxy
        assert repr(proxy) == 'mappingproxy(%r)' % mapping
        assert proxy.keys() == mapping.keys()
        raises(TypeError, "proxy['a'] = 4")
        raises(TypeError, "del proxy['a']")
        raises(AttributeError, "proxy.clear()")
        #
        class D(dict):
            def copy(self): return 3
        proxy = dictproxy(D(a=1, b=2, c=3))
        assert proxy.copy() == 3
        #
        raises(TypeError, dictproxy, 3)
        raises(TypeError, dictproxy, [3])
        #
        {}.update(proxy)

class AppTestUserObjectMethodCache(AppTestUserObject):
    spaceconfig = {"objspace.std.withmethodcachecounter": True}

