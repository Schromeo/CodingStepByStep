from collections import defaultdict
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[int], evalints: list[str]) -> list[str]:
        def add(p1, p2):
            p_sum = defaultdict(int, p1)
            for term, coeff in p2.items():
                p_sum[term] += coeff
            return p_sum
        
        def sub(p1,p2):
            p_sub = defaultdict(int, p1)
            for term, coeff in p2.items():
                p_sub[term] -= coeff
            return p_sub
        
        def mul(p1, p2):
            p_prod = defaultdict(int)
            for t1, c1 in p1.items():
                for t2, c2 in p2.items():
                    new_term = tuple(sorted(t1+t2))
                    p_prod[new_term] += c1 * c2
            return p_prod
        
        eval_map = {var: val for var, val in zip(evalvars, evalints)}
        tokens = expression.replace("(", " ( ").replace(")"," ) ").split()
        self.i = 0

        def parse_term():
            left_poly = parse_atom()
            while self.i < len(tokens) and tokens[self.i] == '*':
                self.i += 1
                right_poly = parse_atom()
                left_poly = mul(left_poly, right_poly)
            return left_poly
        
        def parse_expression():
            left_poly = parse_term()
            while self.i < len(tokens) and tokens[self.i] in ('+','-'):
                op = tokens[self.i]
                self.i += 1
                right_poly = parse_term()
                if op == '+':
                    left_poly = add(left_poly, right_poly)
                else:
                    left_poly = sub(left_poly, right_poly)
            return left_poly

        def parse_atom():
            token = tokens[self.i]
            self.i += 1

            if token == '(':
                result_poly = parse_expression()
                self.i += 1
                return result_poly
            elif token.isdigit():
                return defaultdict(int, {(): int(token)})
            else:
                if token in eval_map:
                    return defaultdict(int, {(): eval_map[token]})
                else:
                    return defaultdict(int, {(token,):1})
        
        final_poly = parse_expression()
        terms_list = []
        for term_tuple, coeff in final_poly.items():
            if coeff != 0:
                terms_list.append((len(term_tuple), term_tuple, coeff))
        
        terms_list.sort(key=lambda x: (-x[0], x[1]))

        output = []
        for degree, term_tuple, coeff in terms_list:
            term_str = str(coeff)
            if degree > 0:
                term_str += "*" + "*".join(term_tuple)
            output.append(term_str)
        return output
    
test = Solution()
print(test.basicCalculatorIV("(e + 8) * (e - 8)",[],[]))
print(test.basicCalculatorIV("e - 8 + temperature - pressure",["e", "temperature"],[1,12]))