package com.ryotanada.langapp.retrofit;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.*;

public class APIKindaStuff {
    public interface APIService{

        @Headers({"Content-type: application/json"})
        @POST("/api/post_some_data")
        Call<ResponseBody> getVectors(@Body JsonObject var1);
    }

    public static Gson gson = new GsonBuilder().create();

    private static final Retrofit retrofit = new Retrofit.Builder()
        .baseUrl("http://10.0.0.2:5000")
        .addConverterFactory(GsonConverterFactory.create(gson))
        .build();

    public static APIService service = retrofit.create(APIKindaStuff.APIService.class);
}
