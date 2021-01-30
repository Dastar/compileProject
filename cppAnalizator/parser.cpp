#include <iostream>
#include <stdlib.h> 
#include "parser.h"

namespace CppParser
{
    Parser::Parser(std::string input): 
                m_input(input), m_index(0) {
        m_len = m_input.length();
        m_lookahead = m_input[0];
    }
    
    // Expr -> TermRest
    // Rest -> +TermRest | -TermRest | 0
    // Term -> 0...9
    void Parser::expr(){
        term();
        while (true){
            if (m_lookahead == '+') {
                match('+'); 
                term(); 
                print('+');
            }
            else if (m_lookahead == '-') {
                match('-'); 
                term(); 
                print('-');

            }
            else {
                return;
            }
        }
    }

    void Parser::term(){
        if (isdigit(m_lookahead))
        {
            print(); 
            match(m_lookahead);
        }
        else {
            throw SyntaxException();
        }
    }

    void Parser::match(char t) {
        if (m_index > m_len || m_lookahead != t) {
            throw SyntaxException();
        }
        else {
            m_index++;
            m_lookahead = m_input[m_index];
        }
    }

    void Parser::print(){
        print(m_lookahead);
    }

    void Parser::print(char t) {
        std::cout<<t;
    }
} // namespace CppParser




int main() {
    try
    {
        CppParser::Parser p("1+5-8");
        p.expr(); std::cout<<std::endl;
    }
    catch(CppParser::SyntaxException e)
    {
        std::cerr << e.what() << '\n';
    }
    
    
}
