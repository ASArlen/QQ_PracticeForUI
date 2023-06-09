from behave import *

use_step_matcher('re')


@step('test_0605 (.*)(.*)')
def step_impl(context,condiction1,condiction2):
    context.test1_page.test_0605(condiction1,condiction2)

