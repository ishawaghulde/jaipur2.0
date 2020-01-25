package com.example.jaipur;

public class Review {
    private float overall;
    private float illum;
    private float population;
    private float quality;
    private String comment;
    private String streets;

    public Review(float overall, float illum,float population,  float quality, String comment, String streets) {
        this.overall = overall;
        this.illum = illum;
        this.population = population;
        this.quality = quality;
        this.comment = comment;
        this.streets = streets;
    }

    public float getOverall() {
        return overall;
    }

    public float getIllum() {
        return illum;
    }

    public float getPopulation() {
        return population;
    }

    public float getQuality() {
        return quality;
    }

    public String getComment() {
        return comment;
    }

    public String getStreets() {
        return streets;
    }

}
