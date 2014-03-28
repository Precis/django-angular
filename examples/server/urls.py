# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from server.views import SubscribeViewWithFormValidation, SubscribeViewWithModelForm,\
    SubscribeViewWithModelFormAndValidation, Ng3WayDataBindingView, NgFormDataValidView,\
    SimpleCRUDView, ValidatedCRUDView


urlpatterns = patterns('',
    url(r'^form_validation/$', SubscribeViewWithFormValidation.as_view(),
        name='djng_form_validation'),
    url(r'^model_form/$', SubscribeViewWithModelForm.as_view(),
        name='djng_model_form'),
    url(r'^model_form_validation/$', SubscribeViewWithModelFormAndValidation.as_view(),
        name='djng_model_form_validation'),
    url(r'^threeway_databinding/$', Ng3WayDataBindingView.as_view(),
        name='djng_3way_databinding'),
    url(r'^form_data_valid', NgFormDataValidView.as_view(), name='form_data_valid'),
    url(r'^model_form_with_crud/$', ValidatedCRUDView.as_view(), name='djng_model_form_crud_response'),
    url(r'^crud/simplemodel$', SimpleCRUDView.as_view(), name='djng_simple_crud'),
)
