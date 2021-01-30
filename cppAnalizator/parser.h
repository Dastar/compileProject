#include <string>

namespace CppParser
{
    class Parser {
    public:
        Parser(std::string input);
        void expr();
        void term();
        void match(char t);
    private:
        void print();
        void print(char t);
    private:
        std::string m_input;
        char m_lookahead;
        int m_index;
        int m_len;
    };    

    class SyntaxException: public std::exception {
        public:
        const char * what() {
            return "\nSyntax Error";
        }
    };
} // namespace CppParser

