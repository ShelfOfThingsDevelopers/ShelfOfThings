package com.iot.shelfofthings.engine;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;

/** Class that implements connection with server
 * 
 * @author dmitry
 *
 */
public class Connection {

	private static Connection instance;
	private UpdateThread updateThread;
	
	private Connection()
	{
		updateThread = new UpdateThread();	
	}
	
	public static Connection getInstance()
	{
		if(instance == null)
		{
			return new Connection();
		}
		return instance;
	}
	
	public void sendLightCommand(String bookId)
	{
		Message msg = new Message();
		Bundle data = new Bundle();
		data.putString("id", bookId);
		msg.setData(data);
		highlightHandler.sendMessage(msg);
	}
	
	class UpdateThread implements Runnable
	{
		private Thread thread;

		UpdateThread()
		{
			thread = new Thread(this, "UpdateThread");
			thread.start(); 
		}
		
		@Override
		public void run() {
			
			while(true)
			{				
				// TODO Server listening
				
			}
		}
	}
	
	private final Handler highlightHandler = new Handler() {
		@Override
        public void handleMessage(Message inputMessage) {
			int id = Integer.parseInt(inputMessage.getData().getString("id"));
			// TODO send id to server
		}
	};
}
