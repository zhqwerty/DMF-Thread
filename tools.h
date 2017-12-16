#ifndef _TOOLS_
#define _TOOLS_

#include <chrono>

class Timer
{
    typedef std::chrono::steady_clock::time_point   tp;
    typedef std::chrono::duration<double>           dd;
    typedef std::chrono::steady_clock               sc;
public:
    tp start;
    tp end;
    dd span;
    double duration;
    Timer(): start(sc::now()), span(dd(0)){}
    void Tick(){
        start = sc::now();
    }
    void Tock(){
        end = sc::now();
        span += std::chrono::duration_cast<dd>(end - start);
        duration = span.count();
        span = dd(0);
    }
};

template<typename T>
T max_element(std::vector<T> vec) {
  T max_val = vec[0];
    for(int i = 1; i < vec.size(); i++) {
      if (max_val < vec[i])
        max_val = vec[i];
    }
  return max_val;
}

template<class T>
int sign(T x){
    if (x == 0) return 0;
    return x > 0 ? 1 : -1;
}

#endif
