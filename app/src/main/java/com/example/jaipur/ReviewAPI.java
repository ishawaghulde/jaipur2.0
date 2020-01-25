package com.example.jaipur;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ReviewAPI {
    @POST("items")
    Call<Review> createReview(@Body Review review);
}
