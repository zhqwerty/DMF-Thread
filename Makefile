./PHONY: single_thread
single_thread: single_thread.cpp examples.cpp fvector.cpp simple_random.cpp timer.cpp	
	g++ -std=c++11 -o single_thread single_thread.cpp examples.cpp fvector.cpp simple_random.cpp timer.cpp

clean:
	@rm -f single_thread