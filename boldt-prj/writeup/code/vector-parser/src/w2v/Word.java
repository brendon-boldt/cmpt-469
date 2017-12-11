package w2v;

import java.util.ArrayList;
import java.util.List;

public class Word {
	
	final ArrayList<Double> scalars;
	final String name;
	
	public Word(String line) {
		String[] vals = line.split(" ");
		this.name = vals[0];
		this.scalars = new ArrayList<>();
		for (int i = 1; i < vals.length; ++i) {
			this.scalars.add(Double.valueOf(vals[i]));
		}
	}
	
	public Word(String name, ArrayList<Double> scalars) {
		this.name = name;
		this.scalars = scalars;
	}
	
	public List<Double> unitVector() {
		ArrayList<Double> l = new ArrayList<>();
		double mag = this.mag();
		for (Double x : scalars)
			l.add(x/mag);
		return l;
	}
	
	public double mag() {
		return Math.pow(scalars.stream()
				.reduce(0.0, (a,b) -> a + b*b), 0.5);
	}
	
	public String toString() {
		return name;
	}
}
