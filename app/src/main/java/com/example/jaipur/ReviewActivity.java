package com.example.jaipur;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RatingBar;
import android.widget.Toast;

import es.dmoral.toasty.Toasty;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ReviewActivity extends AppCompatActivity {

//    private RoundCornerProgressBar progressTwo;
    private RatingBar overall;
    private RatingBar population;
    private RatingBar illumination;
    private RatingBar quality;
    private float ofloat;
    private float pfloat;
    private float ifloat;
    private float qfloat;
    private Button submit_btn;
    private EditText commentBox;
    private String comment;
    private String streets;
    private ReviewAPI reviewAPI;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_review);

        overall = findViewById(R.id.overall_rating);
        population = findViewById(R.id.population_rating);
        illumination = findViewById(R.id.illumination_rating);
        quality = findViewById(R.id.quality_rating);
        commentBox = findViewById(R.id.editText);
        submit_btn = findViewById(R.id.submit_btn);




        submit_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ofloat = overall.getRating();
                pfloat = population.getRating();
                ifloat = illumination.getRating();
                qfloat = quality.getRating();
                comment = commentBox.getText().toString();
                streets = "";
                Toast.makeText(ReviewActivity.this, "" + ofloat + " " + pfloat +  " "+ ifloat+ " " + qfloat +  " ", Toast.LENGTH_SHORT).show();
                if(ofloat!=0&&pfloat!=0&&ifloat!=0&&qfloat!=0){
                    insertDetails(ofloat, pfloat, ifloat, qfloat, comment, streets);
                }
//                else{
//
//                    showToast("warn",  "Please enter ratings");
//                }
            }
        });

    }

    private void insertDetails(float ofloat, float pfloat, float ifloat, float qfloat, String comment, String streets ){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://waghulde-products-application.herokuapp.com/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        reviewAPI = retrofit.create(ReviewAPI.class);

        Review review = new Review(ofloat, pfloat, ifloat, qfloat, comment, streets);

        Call<Review> call = reviewAPI.createReview(review);
        call.enqueue(new Callback<Review>() {
            @Override
            public void onResponse(Call<Review> call, Response<Review> response) {
                if(!response.isSuccessful()){
                    showToast("error", response.code() + " : not added to db");
                    return;
                }
                showToast("success", response.code() + " : added to db");
                Intent intent = new Intent(ReviewActivity.this, MainActivity.class);
                startActivity(intent);
            }

            @Override
            public void onFailure(Call<Review> call, Throwable t) {
                showToast("error", t.getMessage());


            }
        });

    }

    private void showToast(String type, String message){
        if(type.equals("warn")){
            Toasty.warning(this, message, Toast.LENGTH_SHORT).show();
            return;
        }
        else if(type.equals("error")){
            Toasty.error(this, message, Toast.LENGTH_SHORT).show();
            return;
        }
        Toasty.success(this, message, Toast.LENGTH_SHORT).show();
    }
}
