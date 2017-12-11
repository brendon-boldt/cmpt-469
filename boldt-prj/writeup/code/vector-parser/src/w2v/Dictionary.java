package w2v;

import java.util.HashMap;

public class Dictionary {
	
	HashMap<String,Word> entries;
	
	public Dictionary(Reader r) {
		this.entries = r.getWords(); 
	}
}
