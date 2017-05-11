# -*- coding: utf-8 -*-

from page_object import PageObject, PageElement
from page_object.elements import Checkbox, Link, Radio, Select, Textbox


class KaskoCalcPage(PageObject):
    URL = "https://guideh.com/fizicheskie-lica/rasschitat-stoimost/kasko/"

    city = Select(id="m_city_i")
    brand = Select(id="m_brand")
    model = Select(id="m_model")
    year = Select(id="m_year")
    cost = Textbox(id="m_coast")
    kpu = Select(id="m_kpu")
    kpu_model = Select(id="m_kpu_model")
    dop_secr = Checkbox(id="m_dop_secr")
    dop_igla = Checkbox(id="m_dop_igla")
    dop_mark = Checkbox(id="m_dop_mark")
    less_1000 = Checkbox(id="m_less_1000")
    credit = Checkbox(id="m_credit")
    oldcomp_none = Radio(id="m_oldcomp_0")
    oldcomp_one_year = Radio(id="m_oldcomp_1")
    sto_guide = Radio(id="m_sto_1")
    sto_dealer = Radio(id="m_sto_2")
    franchise = Select(id="m_franchise")
    multidrive = Radio(id="m_driver_1")
    drivers = Radio(id="m_driver_2")
    driver_age = Textbox(id="m_age_0")
    driver_experience = Textbox(id="m_experience_0")
    add_driver = Link(id="g-btn-insured-plus")
    result = PageElement(id="m_result_value")
