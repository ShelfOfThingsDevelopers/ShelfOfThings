package com.iot.shelfofthings.engine;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteException;
import android.database.sqlite.SQLiteOpenHelper;

/** Main database class
 * 
 * @author dmitry
 *
 */
public class Database {

	public static String DB_NAME = "db_shelfofthings.sqlite3";
	public static int DB_VERSION = 1;
	
	public static String BOOKS_TABLE = "books_table";
	
	public static String BOOK_ID = "_id";
	public static String BOOK_AUTHOR = "book_author";
	public static String BOOK_NAME = "book_name";
	public static String BOOKSHELF_POSITION = "bookshelf_position";
	
	public static String CREATE_BOOKS_TABLE = "create table " + BOOKS_TABLE +
				"(" + BOOK_ID + " INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " + 
					  BOOK_AUTHOR + " VARCHAR NOT NULL, " + 
					  BOOK_NAME + " VARCHAR NOT NULL, " +
					  BOOKSHELF_POSITION + " VARCHAR);";
	
	public SQLiteDatabase database;
	private DbOpenHelper dbHelper;
	private final Context mContext;
	
	private static Database instance;
	
	private Database(Context context)
	{
		mContext = context;
		dbHelper = new DbOpenHelper(mContext, DB_NAME, null, DB_VERSION);
		try {
			database = dbHelper.getWritableDatabase();
		}
		catch (SQLiteException ex){
			database = dbHelper.getReadableDatabase();
		}	
	}
	
	public static Database getInstance(Context context)
	{
		if(instance == null)
		{
			return new Database(context);
		}
		return instance;
	}
	
	/** Class for database creation
	 * 
	 * @author dmitry
	 *
	 */
	private class DbOpenHelper extends SQLiteOpenHelper{

		public DbOpenHelper(Context context, String name, CursorFactory factory,
				int version) {
			super(context, name, factory, version);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onCreate(SQLiteDatabase db) {
			db.execSQL(CREATE_BOOKS_TABLE);
			
		}
		
		@Override
		public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
			// TODO Auto-generated method stub
			
		}
	}
}
