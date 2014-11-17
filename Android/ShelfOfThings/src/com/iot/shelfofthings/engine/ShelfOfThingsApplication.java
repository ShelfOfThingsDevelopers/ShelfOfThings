package com.iot.shelfofthings.engine;

import android.app.Application;

public class ShelfOfThingsApplication extends Application{

	public void onCreate()
	{
		super.onCreate();
		Connection.getInstance();
	}
}
