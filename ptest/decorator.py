__author__ = 'karl.gong'

from .enumeration import PDecoratorType


def BeforeSuite(enabled=True, description="", timeout=0, **custom_args):
    """
        The BeforeSuite test fixture, it will be executed before test suite started.

    :param enabled: enable or disable this test fixture.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.BeforeSuite
        func.__enabled__ = enabled
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def AfterSuite(enabled=True, always_run=False, description="", timeout=0, **custom_args):
    """
        The AfterSuite test fixture, it will be executed after test suite finished.

    :param enabled: enable or disable this test fixture.
    :param always_run: if set to true, this test fixture will be run even if the @BeforeSuite is failed. Otherwise, this test fixture will be skipped.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.AfterSuite
        func.__enabled__ = enabled
        func.__always_run__ = always_run
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def TestClass(enabled=True, run_mode="parallel", description="", **custom_args):
    """
        The TestClass decorator, it is used to mark a class as TestClass.

    :param enabled: enable or disable this test class.
    :param run_mode: the run mode of all the test cases in this test class. If set to "parallel", all the test cases will be run by multiple threads. If set to "singleline", all the test cases will be only run by one thread.
    :param description: the description of this test class.
    :param custom_args: the custom arguments of this test class.
    """

    def tracer(cls):
        cls.__pd_type__ = PDecoratorType.TestClass
        cls.__enabled__ = enabled
        cls.__run_mode__ = run_mode
        cls.__description__ = description
        cls.__custom_args__ = custom_args
        return cls

    return tracer


def BeforeClass(enabled=True, description="", timeout=0, **custom_args):
    """
        The BeforeClass test fixture, it will be executed before test class started.

    :param enabled: enable or disable this test fixture.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.BeforeClass
        func.__enabled__ = enabled
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def AfterClass(enabled=True, always_run=False, description="", timeout=0, **custom_args):
    """
        The AfterClass test fixture, it will be executed after test class finished.

    :param enabled: enable or disable this test fixture.
    :param always_run: if set to true, this test fixture will be run even if the @BeforeClass is failed. Otherwise, this test fixture will be skipped.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.AfterClass
        func.__enabled__ = enabled
        func.__always_run__ = always_run
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def BeforeGroup(enabled=True, group="DEFAULT", description="", timeout=0, **custom_args):
    """
        The BeforeGroup test fixture, it will be executed before test group started.

    :param enabled: enable or disable this test fixture.
    :param group: the group that this test fixture is belong to.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.BeforeGroup
        func.__enabled__ = enabled
        func.__group__ = group
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def AfterGroup(enabled=True, always_run=False, group="DEFAULT", description="", timeout=0, **custom_args):
    """
        The AfterGroup test fixture, it will be executed after test group finished.

    :param enabled: enable or disable this test fixture.
    :param always_run: if set to true, this test fixture will be run even if the @BeforeGroup is failed. Otherwise, this test fixture will be skipped.
    :param group: the group that this test fixture is belong to.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.AfterGroup
        func.__enabled__ = enabled
        func.__always_run__ = always_run
        func.__group__ = group
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def Test(enabled=True, tags=[], group="DEFAULT", description="", timeout=0, **custom_args):
    """
        The Test decorator, it is used to mark a test as Test.

    :param enabled: enable or disable this test.
    :param tags: the tags of this test. It can be string (separated by comma) or list or tuple.
    :param group: the group that this test is belong to.
    :param description: the description of this test.
    :param timeout: the timeout of this test (in seconds).
    :param custom_args: the custom arguments of this test.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.Test
        func.__enabled__ = enabled
        func.__group__ = group
        func.__description__ = description
        func.__tags__ = tags
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def BeforeMethod(enabled=True, group="DEFAULT", description="", timeout=0, **custom_args):
    """
        The BeforeMethod test fixture, it will be executed before test started.

    :param enabled: enable or disable this test fixture.
    :param group: the group that this test fixture is belong to.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.BeforeMethod
        func.__enabled__ = enabled
        func.__group__ = group
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func


def AfterMethod(enabled=True, always_run=False, group="DEFAULT", description="", timeout=0, **custom_args):
    """
        The AfterMethod test fixture, it will be executed after test finished.

    :param enabled: enable or disable this test fixture.
    :param always_run: if set to true, this test fixture will be run even if the @BeforeMethod is failed. Otherwise, this test fixture will be skipped.
    :param group: the group that this test fixture is belong to.
    :param description: the description of this test fixture.
    :param timeout: the timeout of this test fixture (in seconds).
    :param custom_args: the custom arguments of this test fixture.
    """

    def handle_func(func):
        func.__pd_type__ = PDecoratorType.AfterMethod
        func.__enabled__ = enabled
        func.__always_run__ = always_run
        func.__group__ = group
        func.__description__ = description
        func.__timeout__ = timeout
        func.__custom_args__ = custom_args
        return func

    return handle_func
