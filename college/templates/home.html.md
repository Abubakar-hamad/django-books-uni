{% extends 'index.html' %}
{% load static %}

{% block my_code %}

<div class="slider_area">
    <div class="single_slider  d-flex align-items-center slider_bg_1">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-7 col-md-6">
                    <div class="slider_text">
                        <h5 class="wow fadeInLeft" data-wow-duration="1s" data-wow-delay=".2s"> +500 كتاب في شتى
                            المجالات </h5>
                        <h3 class="wow fadeInLeft" data-wow-duration="1s" data-wow-delay=".3s">مكتبة الجامعة الرقمية
                        </h3>
                        <p class="wow fadeInLeft" data-wow-duration="1s" data-wow-delay=".4s">أضف المزيد الى معلوماتك
                            اذا كنت طالب في جامعتنا او من خارجها من خلال مكتبة الجامعة الرقمية</p>
                        <!-- <div class="sldier_btn wow fadeInLeft" data-wow-duration="1s" data-wow-delay=".5s">
                            <a href="#" class="boxed-btn3">Upload your Resume</a>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="ilstration_img wow fadeInRight d-none d-lg-block text-right" data-wow-duration="1s"
        data-wow-delay=".2s">
        <img src="img/banner/illustration.png" alt="">
    </div>
</div>

<!-- popular_catagory_area_start  -->
<div class="popular_catagory_area">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section_title mb-40">
                    <h3 style="text-align: center;">الكليــــات </h3>
                </div>
            </div>
        </div>
        <div class="row">
            {% for coll in colleges_list %}



            <div class="col-lg-4 col-xl-3 col-md-6">
                <div class="single_catagory">
                    <h4 style="text-align: center;">{{coll.CLtitle}}</h4>
                    <p style="text-align: center;"> عدد اﻷقســام <span>{{coll.CLdepart}}</span> </p>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
<!-- popular_catagory_area_end  -->


<!-- testimonial_area  -->
<div class="testimonial_area  ">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section_title text-center mb-40">
                    <h3>Testimonial</h3>
                </div>
            </div>
            <div class="col-xl-12">
                <div class="testmonial_active owl-carousel">

                    {% for br in branch_all %}
                    <div class="single_carousel">
                        <div class="row">
                            <div class="col-lg-11">
                                <div class="single_testmonial d-flex align-items-center">
                                    <div class="thumb">
                                        <img src="{% static 'img/testmonial/author.png' %}" alt="">
                                        <div class="quote_icon">
                                            <i class="Flaticon flaticon-quote"></i>
                                        </div>
                                    </div>
                                    <div class="info">
                                        <p>{{br.BRtitle}}</p>
                                        <span>- Micky Mouse</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endfor %}



                </div>
            </div>
        </div>
    </div>
</div>
<!-- /testimonial_area  -->

<!-- featured_candidates_area_start  -->
<div class="featured_candidates_area">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section_title text-center mb-40">
                    <h3>الفــــرو ع</h3>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12">
                <div class="candidate_active owl-carousel">


                    {% for br in branch_all %}



                    <div class="single_candidates text-center">
                        <div class="thumb">
                            <img src="{{br.BRImg.url}}" alt="">
                        </div>
                        <h4>{{br.BRtitle}}</h4>

                    </div>
                    {% endfor %}

                </div>
            </div>
        </div>
    </div>
</div>
<!-- featured_candidates_area_end  -->




{% endblock my_code %}