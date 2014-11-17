package com.iot.shelfofthings;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.iot.shelfofthings.engine.BookContent;
import com.iot.shelfofthings.engine.Connection;

/**
 * A fragment representing a single Book detail screen. This fragment is either
 * contained in a {@link BookListActivity} in two-pane mode (on tablets) or a
 * {@link BookDetailActivity} on handsets.
 */
public class BookDetailFragment extends Fragment {
	/**
	 * The fragment argument representing the item ID that this fragment
	 * represents.
	 */
	public static final String ARG_ITEM_ID = "item_id";

	/**
	 * The Book content this fragment is presenting.
	 */
	private BookContent.BookItem mItem;

	/**
	 * Mandatory empty constructor for the fragment manager to instantiate the
	 * fragment (e.g. upon screen orientation changes).
	 */
	public BookDetailFragment() {
	}

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

		if (getArguments().containsKey(ARG_ITEM_ID)) {
			// Load the Book content specified by the fragment
			// arguments. In a real-world scenario, use a Loader
			// to load content from a content provider.
			mItem = BookContent.ITEM_MAP.get(getArguments().getString(
					ARG_ITEM_ID));
		}
	}

	@Override
	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		View rootView = inflater.inflate(R.layout.fragment_book_detail,
				container, false);

		// Show the Book content as text in a TextView.
		if (mItem != null) {
			((TextView) rootView.findViewById(R.id.book_author))
					.setText(mItem.author);
			((TextView) rootView.findViewById(R.id.book_name))
					.setText(mItem.bookName);
			((TextView) rootView.findViewById(R.id.bookshelf_position))
					.setText(mItem.bookshelfPosition);
		}

		return rootView;
	}
	
	public void onHighlightBook(View v)
	{
		Connection connection = Connection.getInstance();
		connection.sendLightCommand(mItem.id);
		Toast.makeText(getActivity(), "as", Toast.LENGTH_SHORT).show();
	}
}
