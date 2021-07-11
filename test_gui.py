import pytest
from PySide2 import QtCore

import plotter


@pytest.fixture
def app(qtbot):
    test_app = plotter.PlotWidget()
    qtbot.addWidget(test_app)

    return test_app

@pytest.fixture(scope='function', autouse=True)
def first_app(app, request):
    request.instance.app = app

class Test_function:

    def test_func_label(self, request):
        assert request.instance.app.func_label.text() == "Function: "

    def test_function_text_whitelist(self, request):
        assert request.instance.app.function.text() == "x"

    def test_function_textbox_blacklist(self, request):
        assert request.instance.app.function.text() != ""

    def test_editable(self, request):
        assert request.instance.app.function.isReadOnly() == False

    def test_enabled(self, request):
        assert request.instance.app.function.isEnabled() == True
    
    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.submit.clicked, timeout=10000):
            request.instance.app.submit.click()


class Test_min_spinbox:

    def test_value(self, request):
        assert request.instance.app.mn.value() == float(-10)
    
    def test_minimum_value(self, request):
        assert request.instance.app.mn.minimum() == float(-1000)

    def test_maximum_value(self, request):
        assert request.instance.app.mn.maximum() == float(1000)

    def test_prefix(self, request):
        assert request.instance.app.mn.prefix() == "min x: "

    def test_editable(self, request):
        assert request.instance.app.mn.isReadOnly() == False

    def test_enabled(self, request):
        assert request.instance.app.mn.isEnabled() == True

    def test_stepdown(self, request):
        request.instance.app.mn.stepBy(-5)
        assert request.instance.app.mn.value() == float(-15)

    def test_stepup(self, request):
        request.instance.app.mn.stepBy(5)
        assert request.instance.app.mn.value() == float(-5)
    
    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.mn.valueChanged, timeout=10000):
            request.instance.app.mn.stepBy(5)

    
class Test_max_spinbox:
    
    def test_value(self, request):
        assert request.instance.app.mx.value() == float(10)
    
    def test_minimum_value(self, request):
        assert request.instance.app.mx.minimum() == float(-1000)

    def test_maximum_value(self, request):
        assert request.instance.app.mx.maximum() == float(1000)

    def test_prefix(self, request):
        assert request.instance.app.mx.prefix() == "max x: "

    def test_editable(self, request):
        assert request.instance.app.mx.isReadOnly() == False

    def test_enabled(self, request):
        assert request.instance.app.mx.isEnabled() == True

    def test_stepdown(self, request):
        request.instance.app.mx.stepBy(-5)
        assert request.instance.app.mx.value() == float(5)

    def test_stepup(self, request):
        request.instance.app.mx.stepBy(5)
        assert request.instance.app.mx.value() == float(15)

    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.mx.valueChanged, timeout=10000):
            request.instance.app.mx.stepBy(5)