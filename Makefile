./PHONY: multiple_thread
multiple_thread: multiple_thread.cpp examples.cpp fvector.cpp simple_random.cpp timer.cpp	
	g++ -std=c++11 -o multiple_thread multiple_thread.cpp examples.cpp fvector.cpp simple_random.cpp timer.cpp

clean:
	@rm -f multiple_thread
