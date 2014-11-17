package com.iot.shelfofthings.engine;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** Class that represents book content
 * 
 * @author dmitry
 *
 */
public class BookContent {

	/**
	 * An array of book items.
	 */
	public static List<BookItem> ITEMS = new ArrayList<BookItem>();

	/**
	 * A map of book items, by ID.
	 */
	public static Map<String, BookItem> ITEM_MAP = new HashMap<String, BookItem>();

	static {
		// Add 3 sample items.
		addItem(new BookItem("1", "Lev Tolstoy", "War and Peace", "Pos1"));
		addItem(new BookItem("2", "Lev Tolstoy", "Anna Karenina", "Pos2"));
		addItem(new BookItem("3", "Anthony Burgess", "Clockwork Orange", "Pos3"));
		
		// TODO : load items from database (in Database class)
	}

	public static void addItem(BookItem item) {
		ITEMS.add(item);
		ITEM_MAP.put(item.id, item);
	}

	/**
	 * A Book item representing a piece of content.
	 */
	public static class BookItem {
		public String id;
		public String author;
		public String bookName;
		public String bookshelfPosition;
		public String content;
		
		public BookItem(String id, String author, String bookName, String bookshelfPosition) {
			this.id = id;
			this.author = author;
			this.bookName = bookName;
			this.bookshelfPosition = bookshelfPosition;
			this.content = "ID " + id + ": " + author + " - \"" + bookName + "\"";
		}
		
		@Override
		public String toString()
		{
			return content;
		}
	}
}

