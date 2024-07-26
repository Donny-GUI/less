match node.__class__.__name__:
    case 'Assign':
        match pattern:
            case []:
    case 'Method':
        match pattern:
            case [['source', Name], ['name', Name], ['body', Block]]:
                source = self.convert_Name(node.source)
                name = self.convert_Name(node.name)
                body = self.convert_Block(node.body)
    case 'Name':
        match pattern:
            case [['id', str]]:
                id = self.convert_str(node.id)
    case 'Block':
        match pattern:
            case []:
    case 'If':
        match pattern:
            case [['test', ULNotOp], ['body', Block]]:
                test = self.convert_ULNotOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', Index], ['body', Block], ['orelse', Block]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULNotOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_ULNotOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULNotOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_ULNotOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Index], ['body', Block]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
            case [['test', EqToOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', AndLoOp], ['body', Block]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', EqToOp], ['body', Block]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', AndLoOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Name], ['body', Block], ['orelse', Block]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Name], ['body', Block]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
            case [['test', ULengthOP], ['body', Block]]:
                test = self.convert_ULengthOP(node.test)
                body = self.convert_Block(node.body)
            case [['test', OrLoOp], ['body', Block]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', NotEqToOp], ['body', Block]]:
                test = self.convert_NotEqToOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', GreaterThanOp], ['body', Block]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', EqToOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', AndLoOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Call], ['body', Block]]:
                test = self.convert_Call(node.test)
                body = self.convert_Block(node.body)
            case [['test', Index], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', LessThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_LessThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', LessOrEqThanOp], ['body', Block]]:
                test = self.convert_LessOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', LessThanOp], ['body', Block]]:
                test = self.convert_LessThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', LessThanOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_LessThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', OrLoOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULengthOP], ['body', Block], ['orelse', Block]]:
                test = self.convert_ULengthOP(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', GreaterOrEqThanOp], ['body', Block]]:
                test = self.convert_GreaterOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', Invoke], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Invoke(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', GreaterThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', GreaterThanOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Invoke], ['body', Block]]:
                test = self.convert_Invoke(node.test)
                body = self.convert_Block(node.body)
            case [['test', LessOrEqThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_LessOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', OrLoOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', NotEqToOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_NotEqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULengthOP], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_ULengthOP(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', GreaterOrEqThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_GreaterOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Call], ['body', Block], ['orelse', Block]]:
                test = self.convert_Call(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', FalseExpr], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_FalseExpr(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Name], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', GreaterOrEqThanOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_GreaterOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Invoke], ['body', Block], ['orelse', Block]]:
                test = self.convert_Invoke(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', TrueExpr], ['body', Block], ['orelse', Block]]:
                test = self.convert_TrueExpr(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Call], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Call(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
    case 'ULNotOp':
        match pattern:
            case [['operand', Name]]:
                operand = self.convert_Name(node.operand)
            case [['operand', Index]]:
                operand = self.convert_Index(node.operand)
            case [['operand', ULNotOp]]:
                operand = self.convert_ULNotOp(node.operand)
            case [['operand', OrLoOp]]:
                operand = self.convert_OrLoOp(node.operand)
            case [['operand', Call]]:
                operand = self.convert_Call(node.operand)
            case [['operand', Invoke]]:
                operand = self.convert_Invoke(node.operand)
            case [['operand', AndLoOp]]:
                operand = self.convert_AndLoOp(node.operand)
            case [['operand', EqToOp]]:
                operand = self.convert_EqToOp(node.operand)
            case [['operand', ULengthOP]]:
                operand = self.convert_ULengthOP(node.operand)
    case 'Index':
        match pattern:
            case [['idx', Name], ['value', Index]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Name], ['value', Name]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', OrLoOp], ['value', Index]]:
                idx = self.convert_OrLoOp(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Index], ['value', Index]]:
                idx = self.convert_Index(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Number], ['value', Index]]:
                idx = self.convert_Number(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Number], ['value', Name]]:
                idx = self.convert_Number(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Invoke], ['value', Index]]:
                idx = self.convert_Invoke(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Name], ['value', Invoke]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_Invoke(node.value)
            case [['idx', ULengthOP], ['value', Name]]:
                idx = self.convert_ULengthOP(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Index], ['value', Name]]:
                idx = self.convert_Index(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Concat], ['value', Index]]:
                idx = self.convert_Concat(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', String], ['value', Index]]:
                idx = self.convert_String(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', ULengthOP], ['value', Index]]:
                idx = self.convert_ULengthOP(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', AddOp], ['value', Index]]:
                idx = self.convert_AddOp(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Name], ['value', OrLoOp]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_OrLoOp(node.value)
            case [['idx', String], ['value', Name]]:
                idx = self.convert_String(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Name], ['value', Table]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_Table(node.value)
            case [['idx', Concat], ['value', Name]]:
                idx = self.convert_Concat(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Name], ['value', Call]]:
                idx = self.convert_Name(node.idx)
                value = self.convert_Call(node.value)
            case [['idx', Number], ['value', Call]]:
                idx = self.convert_Number(node.idx)
                value = self.convert_Call(node.value)
            case [['idx', SubOp], ['value', Index]]:
                idx = self.convert_SubOp(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', ModOp], ['value', Index]]:
                idx = self.convert_ModOp(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Call], ['value', Index]]:
                idx = self.convert_Call(node.idx)
                value = self.convert_Index(node.value)
            case [['idx', Call], ['value', Name]]:
                idx = self.convert_Call(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', OrLoOp], ['value', Name]]:
                idx = self.convert_OrLoOp(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Invoke], ['value', Name]]:
                idx = self.convert_Invoke(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', SubOp], ['value', Name]]:
                idx = self.convert_SubOp(node.idx)
                value = self.convert_Name(node.value)
            case [['idx', Index], ['value', Table]]:
                idx = self.convert_Index(node.idx)
                value = self.convert_Table(node.value)
    case 'OrLoOp':
        match pattern:
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', AndLoOp], ['right', Table]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', Index], ['right', Table]]:
                left = self.convert_Index(node.left)
                right = self.convert_Table(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', AndLoOp], ['right', Index]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', AndLoOp], ['right', Call]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', AndLoOp], ['right', String]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_String(node.right)
            case [['left', Name], ['right', Table]]:
                left = self.convert_Name(node.left)
                right = self.convert_Table(node.right)
            case [['left', AndLoOp], ['right', Number]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', EqToOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', EqToOp], ['right', EqToOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', ULNotOp], ['right', Index]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', ULNotOp], ['right', ULengthOP]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', AndLoOp], ['right', UMinusOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', EqToOp], ['right', Index]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Nil]]:
                left = self.convert_Call(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Index], ['right', Nil]]:
                left = self.convert_Index(node.left)
                right = self.convert_Nil(node.right)
            case [['left', AndLoOp], ['right', Nil]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Nil(node.right)
            case [['left', EqToOp], ['right', AndLoOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', OrLoOp], ['right', AndLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', AndLoOp], ['right', AndLoOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', AndLoOp], ['right', ULNotOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', Call]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', String]]:
                left = self.convert_Name(node.left)
                right = self.convert_String(node.right)
            case [['left', OrLoOp], ['right', LessThanOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', ULNotOp], ['right', ULNotOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', OrLoOp], ['right', Table]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', AndLoOp], ['right', Name]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', LessThanOp], ['right', EqToOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', OrLoOp], ['right', GreaterThanOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', Index], ['right', NotEqToOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', Name], ['right', AndLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', ULNotOp], ['right', LessThanOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', ULengthOP]]:
                left = self.convert_Call(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', AndLoOp], ['right', EqToOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', EqToOp], ['right', Call]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', GreaterThanOp], ['right', GreaterThanOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', Invoke], ['right', Invoke]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', EqToOp], ['right', TrueExpr]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', AndLoOp], ['right', FalseExpr]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', OrLoOp], ['right', String]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_String(node.right)
            case [['left', Index], ['right', AndLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', OrLoOp], ['right', UMinusOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', AndLoOp], ['right', MultOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', NotEqToOp], ['right', ULNotOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Index], ['right', EqToOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', AndLoOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', Index], ['right', GreaterThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', NotEqToOp], ['right', EqToOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', ULNotOp], ['right', NotEqToOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', OrLoOp], ['right', ULengthOP]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', GreaterThanOp], ['right', ULengthOP]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Call], ['right', String]]:
                left = self.convert_Call(node.left)
                right = self.convert_String(node.right)
            case [['left', AndLoOp], ['right', Invoke]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', OrLoOp], ['right', NotEqToOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', NotEqToOp], ['right', NotEqToOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', ULNotOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', GreaterOrEqThanOp], ['right', LessThanOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', Index], ['right', UMinusOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', OrLoOp], ['right', ULNotOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Invoke], ['right', String]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_String(node.right)
            case [['left', ULNotOp], ['right', GreaterThanOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', EqToOp], ['right', NotEqToOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', AndLoOp], ['right', OrLoOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', ULNotOp], ['right', AndLoOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', OrLoOp], ['right', Nil]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Nil(node.right)
            case [['left', AndLoOp], ['right', ULengthOP]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', FalseExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Index], ['right', AnonymousFunction]]:
                left = self.convert_Index(node.left)
                right = self.convert_AnonymousFunction(node.right)
            case [['left', GreaterOrEqThanOp], ['right', Name]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', AndLoOp], ['right', NotEqToOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', NotEqToOp], ['right', GreaterThanOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', LessThanOp], ['right', LessThanOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', NotEqToOp], ['right', Name]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Nil]]:
                left = self.convert_Name(node.left)
                right = self.convert_Nil(node.right)
            case [['left', AndLoOp], ['right', AddOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', OrLoOp], ['right', Name]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', ULNotOp], ['right', TrueExpr]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', LessThanOp], ['right', NotEqToOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', LessThanOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', ULNotOp], ['right', EqToOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', LessOrEqThanOp], ['right', Index]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', LessOrEqThanOp], ['right', ULengthOP]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', NotEqToOp], ['right', AndLoOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', Index], ['right', LessOrEqThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', Name], ['right', FalseExpr]]:
                left = self.convert_Name(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Name], ['right', AddOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', GreaterThanOp], ['right', LessThanOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', ULNotOp], ['right', Name]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', ULNotOp], ['right', LessOrEqThanOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', NotEqToOp], ['right', LessThanOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', Name], ['right', ULNotOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', ULengthOP], ['right', ULengthOP]]:
                left = self.convert_ULengthOP(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', AndLoOp], ['right', FloatDivOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', NotEqToOp], ['right', Index]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', GreaterThanOp], ['right', AndLoOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', GreaterThanOp], ['right', Index]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Table]]:
                left = self.convert_Call(node.left)
                right = self.convert_Table(node.right)
            case [['left', OrLoOp], ['right', AddOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', ULNotOp], ['right', OrLoOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', EqToOp], ['right', ULengthOP]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Concat]]:
                left = self.convert_Index(node.left)
                right = self.convert_Concat(node.right)
            case [['left', EqToOp], ['right', ULNotOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
    case 'String':
        match pattern:
            case [['s', str]]:
                s = self.convert_str(node.s)
    case 'Table':
        match pattern:
            case []:
    case 'Call':
        match pattern:
            case [['func', Name]]:
                func = self.convert_Name(node.func)
            case [['func', Index]]:
                func = self.convert_Index(node.func)
            case [['func', Call]]:
                func = self.convert_Call(node.func)
    case 'LocalAssign':
        match pattern:
            case []:
    case 'AndLoOp':
        match pattern:
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', EqToOp], ['right', Call]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', AndLoOp], ['right', Index]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', EqToOp], ['right', EqToOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', ULNotOp], ['right', Index]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', EqToOp], ['right', Index]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', String]]:
                left = self.convert_Name(node.left)
                right = self.convert_String(node.right)
            case [['left', Name], ['right', ULNotOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', GreaterThanOp], ['right', Concat]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Concat(node.right)
            case [['left', AndLoOp], ['right', NotEqToOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', ULNotOp], ['right', ULNotOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', EqToOp], ['right', ULNotOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', AndLoOp], ['right', ULengthOP]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', NotEqToOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', Index], ['right', GreaterOrEqThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', EqToOp], ['right', LessThanOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', AndLoOp], ['right', EqToOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', EqToOp], ['right', Invoke]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Index], ['right', ULNotOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Index], ['right', Invoke]]:
                left = self.convert_Index(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Index], ['right', EqToOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', EqToOp], ['right', Name]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', AndLoOp], ['right', String]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_String(node.right)
            case [['left', AndLoOp], ['right', Number]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', AndLoOp], ['right', ULNotOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', ULNotOp], ['right', OrLoOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', EqToOp], ['right', OrLoOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', OrLoOp], ['right', ULengthOP]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', AndLoOp], ['right', OrLoOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', EqToOp], ['right', String]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_String(node.right)
            case [['left', ULNotOp], ['right', Number]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', LessOrEqThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', ULNotOp], ['right', NotEqToOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', NotEqToOp], ['right', NotEqToOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', GreaterThanOp], ['right', Index]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', GreaterThanOp], ['right', AddOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', AndLoOp], ['right', Invoke]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', AndLoOp], ['right', Table]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', Index], ['right', AndLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', ULNotOp], ['right', EqToOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', EqToOp], ['right', ULengthOP]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', EqToOp], ['right', Number]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', LessThanOp], ['right', Call]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', NotEqToOp], ['right', ULNotOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', OrLoOp], ['right', String]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_String(node.right)
            case [['left', OrLoOp], ['right', UMinusOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Index], ['right', GreaterThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', EqToOp], ['right', GreaterThanOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', ULengthOP], ['right', Index]]:
                left = self.convert_ULengthOP(node.left)
                right = self.convert_Index(node.right)
            case [['left', AndLoOp], ['right', GreaterThanOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', GreaterThanOp], ['right', String]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_String(node.right)
            case [['left', Index], ['right', LessThanOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', EqToOp], ['right', Table]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', Name], ['right', NotEqToOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', EqToOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', GreaterThanOp], ['right', Call]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', EqToOp], ['right', LessOrEqThanOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', AndLoOp], ['right', LessOrEqThanOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', LessThanOp], ['right', Concat]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_Concat(node.right)
            case [['left', AndLoOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', AndLoOp], ['right', LessThanOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', LessOrEqThanOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', NotEqToOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', NotEqToOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', NotEqToOp], ['right', GreaterThanOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', Call]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Invoke], ['right', EqToOp]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', GreaterThanOp], ['right', GreaterThanOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', OrLoOp], ['right', GreaterThanOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', Call], ['right', EqToOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', NotEqToOp], ['right', AndLoOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', Index], ['right', TrueExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', LessThanOp], ['right', String]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_String(node.right)
            case [['left', NotEqToOp], ['right', Number]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', UMinusOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', AndLoOp], ['right', UMinusOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', EqToOp], ['right', UMinusOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', GreaterThanOp], ['right', Number]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', AndLoOp], ['right', AndLoOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', OrLoOp], ['right', AndLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', NotEqToOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', OrLoOp], ['right', EqToOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', Invoke], ['right', Index]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', UMinusOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', OrLoOp], ['right', Table]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', EqToOp], ['right', NotEqToOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', Name], ['right', Table]]:
                left = self.convert_Name(node.left)
                right = self.convert_Table(node.right)
            case [['left', ULNotOp], ['right', Name]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', GreaterThanOp], ['right', EqToOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', NotEqToOp], ['right', Table]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', EqToOp], ['right', MultOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', GreaterThanOp], ['right', NotEqToOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', ULNotOp], ['right', MultOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', EqToOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', ULNotOp], ['right', FalseExpr]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', FalseExpr], ['right', ULNotOp]]:
                left = self.convert_FalseExpr(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', TrueExpr], ['right', ULNotOp]]:
                left = self.convert_TrueExpr(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', OrLoOp], ['right', ULNotOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', ULNotOp], ['right', String]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_String(node.right)
            case [['left', GreaterThanOp], ['right', MultOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', NotEqToOp], ['right', Index]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', TrueExpr]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', Index], ['right', Table]]:
                left = self.convert_Index(node.left)
                right = self.convert_Table(node.right)
            case [['left', LessThanOp], ['right', ULengthOP]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', GreaterThanOp], ['right', Invoke]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', EqToOp], ['right', FalseExpr]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', EqToOp], ['right', AndLoOp]]:
                left = self.convert_EqToOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', NotEqToOp], ['right', OrLoOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', GreaterThanOp], ['right', UMinusOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', LessThanOp], ['right', Number]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', GreaterThanOp], ['right', OrLoOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', LessThanOp], ['right', Index]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Invoke], ['right', ULNotOp]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Invoke], ['right', OrLoOp]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', LessThanOp], ['right', EqToOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', AndLoOp], ['right', Name]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', EqToOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', NotEqToOp], ['right', SubOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Name], ['right', AddOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', LessThanOp], ['right', GreaterThanOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', LessThanOp], ['right', LessThanOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', GreaterOrEqThanOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', GreaterThanOp], ['right', ULengthOP]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Call], ['right', ULNotOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Call], ['right', NotEqToOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', LessOrEqThanOp], ['right', Name]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', GreaterThanOp], ['right', Name]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', LessOrEqThanOp], ['right', GreaterThanOp]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', AndLoOp], ['right', FalseExpr]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', GreaterOrEqThanOp], ['right', ULNotOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', GreaterThanOp], ['right', SubOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Name], ['right', Invoke]]:
                left = self.convert_Name(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', AndLoOp], ['right', Call]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', AndLoOp], ['right', MultOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', LessOrEqThanOp], ['right', ULNotOp]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', NotEqToOp], ['right', Call]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', GreaterOrEqThanOp], ['right', GreaterThanOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', LessThanOp], ['right', NotEqToOp]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_NotEqToOp(node.right)
            case [['left', NotEqToOp], ['right', EqToOp]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_EqToOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', OrLoOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', ULNotOp], ['right', Table]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', AndLoOp], ['right', SubOp]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', LessOrEqThanOp]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', GreaterThanOp], ['right', ULNotOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', OrLoOp], ['right', Call]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', GreaterThanOp], ['right', LessOrEqThanOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', ULNotOp], ['right', AndLoOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', LessOrEqThanOp], ['right', OrLoOp]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', LessOrEqThanOp], ['right', LessOrEqThanOp]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', Name], ['right', GreaterOrEqThanOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_GreaterOrEqThanOp(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', GreaterThanOp], ['right', LessThanOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_LessThanOp(node.right)
            case [['left', Name], ['right', GreaterThanOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_GreaterThanOp(node.right)
            case [['left', GreaterThanOp], ['right', FloatDivOp]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', GreaterOrEqThanOp], ['right', String]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_String(node.right)
            case [['left', GreaterOrEqThanOp], ['right', Name]]:
                left = self.convert_GreaterOrEqThanOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', OrLoOp], ['right', Name]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', OrLoOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', ULNotOp], ['right', LessOrEqThanOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', NotEqToOp], ['right', String]]:
                left = self.convert_NotEqToOp(node.left)
                right = self.convert_String(node.right)
            case [['left', GreaterThanOp], ['right', Table]]:
                left = self.convert_GreaterThanOp(node.left)
                right = self.convert_Table(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', ULengthOP], ['right', Table]]:
                left = self.convert_ULengthOP(node.left)
                right = self.convert_Table(node.right)
            case [['left', LessThanOp], ['right', Name]]:
                left = self.convert_LessThanOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', ULNotOp], ['right', Call]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', LessOrEqThanOp], ['right', Index]]:
                left = self.convert_LessOrEqThanOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
    case 'Number':
        match pattern:
            case []:
    case 'Return':
        match pattern:
            case []:
    case 'Nil':
        match pattern:
            case []:
    case 'ElseIf':
        match pattern:
            case [['test', EqToOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', EqToOp], ['body', Block]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', AndLoOp], ['body', Block]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', AndLoOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', OrLoOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Index], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Index], ['body', Block]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
            case [['test', OrLoOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Index], ['body', Block], ['orelse', Block]]:
                test = self.convert_Index(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Invoke], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Invoke(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Invoke], ['body', Block]]:
                test = self.convert_Invoke(node.test)
                body = self.convert_Block(node.body)
            case [['test', GreaterThanOp], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', GreaterThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULNotOp], ['body', Block]]:
                test = self.convert_ULNotOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', EqToOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', ULengthOP], ['body', Block], ['orelse', Block]]:
                test = self.convert_ULengthOP(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', LessThanOp], ['body', Block]]:
                test = self.convert_LessThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', OrLoOp], ['body', Block]]:
                test = self.convert_OrLoOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', Name], ['body', Block], ['orelse', Block]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', GreaterThanOp], ['body', Block]]:
                test = self.convert_GreaterThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', NotEqToOp], ['body', Block]]:
                test = self.convert_NotEqToOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', GreaterOrEqThanOp], ['body', Block]]:
                test = self.convert_GreaterOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', AndLoOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Name], ['body', Block]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
            case [['test', NotEqToOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_NotEqToOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Call], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Call(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', Name], ['body', Block], ['orelse', ElseIf]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_ElseIf(node.orelse)
            case [['test', GreaterOrEqThanOp], ['body', Block], ['orelse', Block]]:
                test = self.convert_GreaterOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
                orelse = self.convert_Block(node.orelse)
            case [['test', Call], ['body', Block]]:
                test = self.convert_Call(node.test)
                body = self.convert_Block(node.body)
    case 'EqToOp':
        match pattern:
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', Name], ['right', String]]:
                left = self.convert_Name(node.left)
                right = self.convert_String(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', String]]:
                left = self.convert_Call(node.left)
                right = self.convert_String(node.right)
            case [['left', ModOp], ['right', Number]]:
                left = self.convert_ModOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', FalseExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Invoke], ['right', String]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_String(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', Invoke], ['right', Index]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', Concat]]:
                left = self.convert_Index(node.left)
                right = self.convert_Concat(node.right)
            case [['left', Index], ['right', Nil]]:
                left = self.convert_Index(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Index], ['right', ULNotOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Name], ['right', UMinusOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', ULNotOp], ['right', ULNotOp]]:
                left = self.convert_ULNotOp(node.left)
                right = self.convert_ULNotOp(node.right)
            case [['left', Name], ['right', TrueExpr]]:
                left = self.convert_Name(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Call], ['right', Nil]]:
                left = self.convert_Call(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Name], ['right', Nil]]:
                left = self.convert_Name(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Concat], ['right', Index]]:
                left = self.convert_Concat(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', FalseExpr]]:
                left = self.convert_Name(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Invoke], ['right', Invoke]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Index], ['right', TrueExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', MultOp], ['right', FloatDivOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
    case 'UMinusOp':
        match pattern:
            case [['operand', Index]]:
                operand = self.convert_Index(node.operand)
            case [['operand', Number]]:
                operand = self.convert_Number(node.operand)
            case [['operand', Call]]:
                operand = self.convert_Call(node.operand)
            case [['operand', ULengthOP]]:
                operand = self.convert_ULengthOP(node.operand)
            case [['operand', OrLoOp]]:
                operand = self.convert_OrLoOp(node.operand)
            case [['operand', AddOp]]:
                operand = self.convert_AddOp(node.operand)
            case [['operand', Name]]:
                operand = self.convert_Name(node.operand)
    case 'MultOp':
        match pattern:
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', Number]]:
                left = self.convert_Number(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', Index]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', SubOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Number], ['right', Name]]:
                left = self.convert_Number(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', AddOp], ['right', Name]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', MultOp], ['right', Name]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Number], ['right', OrLoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', Index]]:
                left = self.convert_Number(node.left)
                right = self.convert_Index(node.right)
            case [['left', Number], ['right', Call]]:
                left = self.convert_Number(node.left)
                right = self.convert_Call(node.right)
            case [['left', AddOp], ['right', SubOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', AndLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AndLoOp(node.right)
            case [['left', AndLoOp], ['right', Index]]:
                left = self.convert_AndLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', MultOp], ['right', Call]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Number], ['right', AddOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', MultOp], ['right', ExpoOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', Index]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', FloatDivOp], ['right', Name]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', MultOp], ['right', ULengthOP]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', MultOp], ['right', OrLoOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', MultOp], ['right', SubOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', MultOp], ['right', AddOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Number], ['right', UMinusOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', SubOp], ['right', SubOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Number], ['right', ULengthOP]]:
                left = self.convert_Number(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', SubOp], ['right', FloatDivOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', OrLoOp], ['right', AddOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', AddOp], ['right', Call]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', UMinusOp], ['right', Index]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', UMinusOp], ['right', Call]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', UMinusOp], ['right', Name]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', FloatDivOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', AddOp], ['right', MultOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', FloatDivOp], ['right', Index]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Number], ['right', MultOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', MultOp], ['right', FloatDivOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Invoke], ['right', Index]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Index(node.right)
            case [['left', SubOp], ['right', ULengthOP]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', OrLoOp], ['right', FloatDivOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', MultOp], ['right', MultOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', OrLoOp], ['right', SubOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', OrLoOp], ['right', MultOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', OrLoOp], ['right', Call]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Invoke], ['right', Name]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Name(node.right)
            case [['left', FloatDivOp], ['right', OrLoOp]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', UMinusOp], ['right', Number]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', ExpoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', AddOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', SubOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', FloatDivOp], ['right', Call]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', OrLoOp], ['right', Name]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', ExpoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', SubOp], ['right', OrLoOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', FloatDivOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_FloatDivOp(node.right)
    case 'TrueExpr':
        match pattern:
            case []:
    case 'Invoke':
        match pattern:
            case [['source', Index], ['func', Name]]:
                source = self.convert_Index(node.source)
                func = self.convert_Name(node.func)
            case [['source', Name], ['func', Name]]:
                source = self.convert_Name(node.source)
                func = self.convert_Name(node.func)
            case [['source', Invoke], ['func', Name]]:
                source = self.convert_Invoke(node.source)
                func = self.convert_Name(node.func)
            case [['source', OrLoOp], ['func', Name]]:
                source = self.convert_OrLoOp(node.source)
                func = self.convert_Name(node.func)
            case [['source', String], ['func', Name]]:
                source = self.convert_String(node.source)
                func = self.convert_Name(node.func)
            case [['source', Call], ['func', Name]]:
                source = self.convert_Call(node.source)
                func = self.convert_Name(node.func)
    case 'AnonymousFunction':
        match pattern:
            case [['body', Block]]:
                body = self.convert_Block(node.body)
    case 'AddOp':
        match pattern:
            case [['left', Number], ['right', MultOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', MultOp], ['right', Index]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', Index]]:
                left = self.convert_Number(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', OrLoOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', OrLoOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', AddOp], ['right', MultOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', Name]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', AddOp], ['right', Call]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', FloatDivOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', FloatDivOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', MultOp], ['right', OrLoOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', SubOp], ['right', Index]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', MultOp], ['right', FloatDivOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Number], ['right', ModOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_ModOp(node.right)
            case [['left', Number], ['right', Call]]:
                left = self.convert_Number(node.left)
                right = self.convert_Call(node.right)
            case [['left', UMinusOp], ['right', MultOp]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', MultOp], ['right', MultOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Number], ['right', FloatDivOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Number], ['right', Number]]:
                left = self.convert_Number(node.left)
                right = self.convert_Number(node.right)
            case [['left', FloatDivOp], ['right', MultOp]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', AddOp], ['right', ExpoOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', SubOp], ['right', MultOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', FloatDivOp], ['right', Name]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', AddOp], ['right', FloatDivOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', SubOp], ['right', OrLoOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', Name]]:
                left = self.convert_Number(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', Number], ['right', OrLoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', OrLoOp], ['right', MultOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', FloatDivOp], ['right', FloatDivOp]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', ExpoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', AddOp], ['right', Name]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', FloatDivOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', MultOp], ['right', Name]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', MultOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', OrLoOp], ['right', FloatDivOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', ExpoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', Name], ['right', SubOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
    case 'FloatDivOp':
        match pattern:
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', SubOp], ['right', ULengthOP]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Number], ['right', Index]]:
                left = self.convert_Number(node.left)
                right = self.convert_Index(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', ModOp], ['right', Number]]:
                left = self.convert_ModOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', MultOp], ['right', ULengthOP]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', SubOp], ['right', Call]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', MultOp], ['right', Call]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', Number]]:
                left = self.convert_Number(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', MultOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Number], ['right', Name]]:
                left = self.convert_Number(node.left)
                right = self.convert_Name(node.right)
            case [['left', MultOp], ['right', Index]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', MultOp], ['right', Name]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', SubOp], ['right', SubOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', UMinusOp], ['right', Number]]:
                left = self.convert_UMinusOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', FloatDivOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Number], ['right', FloatDivOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Number], ['right', OrLoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', MultOp], ['right', OrLoOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', ULengthOP]]:
                left = self.convert_Number(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', SubOp], ['right', Index]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', MultOp], ['right', Invoke]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Number], ['right', Call]]:
                left = self.convert_Number(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', ExpoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ExpoOp(node.right)
            case [['left', MultOp], ['right', AddOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', MultOp], ['right', SubOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', AddOp], ['right', Name]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Name(node.right)
    case 'FalseExpr':
        match pattern:
            case []:
    case 'Forin':
        match pattern:
            case [['body', Block]]:
                body = self.convert_Block(node.body)
    case 'SubOp':
        match pattern:
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', MultOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Number], ['right', AddOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Number], ['right', FloatDivOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Number], ['right', Index]]:
                left = self.convert_Number(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', SubOp], ['right', SubOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', Number], ['right', SubOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', SubOp], ['right', MultOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', FloatDivOp], ['right', Name]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', FloatDivOp], ['right', FloatDivOp]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Number], ['right', Number]]:
                left = self.convert_Number(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', FloatDivOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', AddOp], ['right', ULengthOP]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Number], ['right', Name]]:
                left = self.convert_Number(node.left)
                right = self.convert_Name(node.right)
            case [['left', Number], ['right', Call]]:
                left = self.convert_Number(node.left)
                right = self.convert_Call(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', FloatDivOp], ['right', AddOp]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', FloatDivOp], ['right', Index]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', FloatDivOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', MultOp], ['right', MultOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', AddOp], ['right', AddOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Index], ['right', FloatDivOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', OrLoOp], ['right', FloatDivOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', SubOp], ['right', Index]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', MultOp], ['right', Name]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', AddOp], ['right', Call]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', AddOp], ['right', Name]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', OrLoOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', MultOp], ['right', Index]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Number], ['right', OrLoOp]]:
                left = self.convert_Number(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', AddOp], ['right', MultOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Name], ['right', ModOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ModOp(node.right)
            case [['left', Number], ['right', ULengthOP]]:
                left = self.convert_Number(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', SubOp], ['right', FloatDivOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
    case 'While':
        match pattern:
            case [['test', LessThanOp], ['body', Block]]:
                test = self.convert_LessThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', ULNotOp], ['body', Block]]:
                test = self.convert_ULNotOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', EqToOp], ['body', Block]]:
                test = self.convert_EqToOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', AndLoOp], ['body', Block]]:
                test = self.convert_AndLoOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', TrueExpr], ['body', Block]]:
                test = self.convert_TrueExpr(node.test)
                body = self.convert_Block(node.body)
            case [['test', LessOrEqThanOp], ['body', Block]]:
                test = self.convert_LessOrEqThanOp(node.test)
                body = self.convert_Block(node.body)
            case [['test', Name], ['body', Block]]:
                test = self.convert_Name(node.test)
                body = self.convert_Block(node.body)
            case [['test', ULengthOP], ['body', Block]]:
                test = self.convert_ULengthOP(node.test)
                body = self.convert_Block(node.body)
            case [['test', NotEqToOp], ['body', Block]]:
                test = self.convert_NotEqToOp(node.test)
                body = self.convert_Block(node.body)
    case 'LessThanOp':
        match pattern:
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', FloatDivOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', MultOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', SubOp], ['right', SubOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', AddOp], ['right', AddOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Concat], ['right', Concat]]:
                left = self.convert_Concat(node.left)
                right = self.convert_Concat(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Name], ['right', FloatDivOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', FloatDivOp], ['right', Index]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', UMinusOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Index], ['right', UMinusOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', UMinusOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Invoke], ['right', Name]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Name(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Name], ['right', SubOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
    case 'Concat':
        match pattern:
            case [['left', Concat], ['right', LessOrEqThanOp]]:
                left = self.convert_Concat(node.left)
                right = self.convert_LessOrEqThanOp(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', String]]:
                left = self.convert_Call(node.left)
                right = self.convert_String(node.right)
            case [['left', OrLoOp], ['right', Index]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Concat], ['right', String]]:
                left = self.convert_Concat(node.left)
                right = self.convert_String(node.right)
            case [['left', Concat], ['right', Call]]:
                left = self.convert_Concat(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', String]]:
                left = self.convert_Name(node.left)
                right = self.convert_String(node.right)
            case [['left', String], ['right', OrLoOp]]:
                left = self.convert_String(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', String], ['right', Call]]:
                left = self.convert_String(node.left)
                right = self.convert_Call(node.right)
            case [['left', Concat], ['right', OrLoOp]]:
                left = self.convert_Concat(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', String], ['right', Index]]:
                left = self.convert_String(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Concat], ['right', Index]]:
                left = self.convert_Concat(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', String], ['right', Name]]:
                left = self.convert_String(node.left)
                right = self.convert_Name(node.right)
            case [['left', OrLoOp], ['right', OrLoOp]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', String], ['right', Number]]:
                left = self.convert_String(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', OrLoOp], ['right', Name]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Invoke]]:
                left = self.convert_Name(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', Concat], ['right', Name]]:
                left = self.convert_Concat(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', OrLoOp], ['right', String]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_String(node.right)
            case [['left', String], ['right', String]]:
                left = self.convert_String(node.left)
                right = self.convert_String(node.right)
            case [['left', OrLoOp], ['right', Call]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Call(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', String], ['right', AddOp]]:
                left = self.convert_String(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Concat], ['right', FloatDivOp]]:
                left = self.convert_Concat(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', String], ['right', FloatDivOp]]:
                left = self.convert_String(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Concat], ['right', SubOp]]:
                left = self.convert_Concat(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', String], ['right', ULengthOP]]:
                left = self.convert_String(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
    case 'LessOrEqThanOp':
        match pattern:
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', SubOp], ['right', Name]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', AddOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
    case 'ULengthOP':
        match pattern:
            case [['operand', OrLoOp]]:
                operand = self.convert_OrLoOp(node.operand)
            case [['operand', GreaterThanOp]]:
                operand = self.convert_GreaterThanOp(node.operand)
            case [['operand', AddOp]]:
                operand = self.convert_AddOp(node.operand)
            case [['operand', Index]]:
                operand = self.convert_Index(node.operand)
            case [['operand', LessThanOp]]:
                operand = self.convert_LessThanOp(node.operand)
            case [['operand', SubOp]]:
                operand = self.convert_SubOp(node.operand)
            case [['operand', Name]]:
                operand = self.convert_Name(node.operand)
            case [['operand', EqToOp]]:
                operand = self.convert_EqToOp(node.operand)
            case [['operand', AndLoOp]]:
                operand = self.convert_AndLoOp(node.operand)
            case [['operand', GreaterOrEqThanOp]]:
                operand = self.convert_GreaterOrEqThanOp(node.operand)
            case [['operand', LessOrEqThanOp]]:
                operand = self.convert_LessOrEqThanOp(node.operand)
            case [['operand', MultOp]]:
                operand = self.convert_MultOp(node.operand)
            case [['operand', FloatDivOp]]:
                operand = self.convert_FloatDivOp(node.operand)
    case 'SemiColon':
        match pattern:
            case []:
    case 'GreaterThanOp':
        match pattern:
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', SubOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', SubOp], ['right', MultOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', Name]]:
                left = self.convert_Call(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', MultOp], ['right', SubOp]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Index], ['right', UMinusOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', SubOp], ['right', AddOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', AddOp], ['right', Index]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', MultOp]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', MultOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_MultOp(node.right)
            case [['left', Index], ['right', FloatDivOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_FloatDivOp(node.right)
            case [['left', Index], ['right', Call]]:
                left = self.convert_Index(node.left)
                right = self.convert_Call(node.right)
            case [['left', Invoke], ['right', Invoke]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Invoke(node.right)
            case [['left', FloatDivOp], ['right', Name]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
    case 'NotEqToOp':
        match pattern:
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', Name], ['right', String]]:
                left = self.convert_Name(node.left)
                right = self.convert_String(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', FalseExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_FalseExpr(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', Index], ['right', TrueExpr]]:
                left = self.convert_Index(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Nil]]:
                left = self.convert_Name(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Index], ['right', UMinusOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_UMinusOp(node.right)
            case [['left', Call], ['right', Nil]]:
                left = self.convert_Call(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Index], ['right', Nil]]:
                left = self.convert_Index(node.left)
                right = self.convert_Nil(node.right)
            case [['left', Call], ['right', String]]:
                left = self.convert_Call(node.left)
                right = self.convert_String(node.right)
            case [['left', Call], ['right', Call]]:
                left = self.convert_Call(node.left)
                right = self.convert_Call(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Name], ['right', TrueExpr]]:
                left = self.convert_Name(node.left)
                right = self.convert_TrueExpr(node.right)
            case [['left', Index], ['right', Concat]]:
                left = self.convert_Index(node.left)
                right = self.convert_Concat(node.right)
            case [['left', ModOp], ['right', Number]]:
                left = self.convert_ModOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', Call]]:
                left = self.convert_Name(node.left)
                right = self.convert_Call(node.right)
    case 'Fornum':
        match pattern:
            case [['target', Name], ['start', Number], ['stop', Number], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_Number(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', Call], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_Call(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', ULengthOP], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_ULengthOP(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Index], ['stop', Index], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Index(node.start)
                stop = self.convert_Index(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', Index], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_Index(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', ULengthOP], ['stop', Number], ['step', UMinusOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_ULengthOP(node.start)
                stop = self.convert_Number(node.stop)
                step = self.convert_UMinusOp(node.step)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', Name], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_Name(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', SubOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_SubOp(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Index], ['stop', Number], ['step', UMinusOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Index(node.start)
                stop = self.convert_Number(node.stop)
                step = self.convert_UMinusOp(node.step)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', AddOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_AddOp(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', OrLoOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_OrLoOp(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', ULengthOP], ['stop', AddOp], ['step', UMinusOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_ULengthOP(node.start)
                stop = self.convert_AddOp(node.stop)
                step = self.convert_UMinusOp(node.step)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Name], ['stop', ULengthOP], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Name(node.start)
                stop = self.convert_ULengthOP(node.stop)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', Number], ['stop', Number], ['step', UMinusOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_Number(node.start)
                stop = self.convert_Number(node.stop)
                step = self.convert_UMinusOp(node.step)
                body = self.convert_Block(node.body)
            case [['target', Name], ['start', SubOp], ['stop', Number], ['step', UMinusOp], ['body', Block]]:
                target = self.convert_Name(node.target)
                start = self.convert_SubOp(node.start)
                stop = self.convert_Number(node.stop)
                step = self.convert_UMinusOp(node.step)
                body = self.convert_Block(node.body)
    case 'int':
        match pattern:
    case 'GreaterOrEqThanOp':
        match pattern:
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', ULengthOP]]:
                left = self.convert_Index(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Index], ['right', OrLoOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', Index]]:
                left = self.convert_Name(node.left)
                right = self.convert_Index(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Name]]:
                left = self.convert_Index(node.left)
                right = self.convert_Name(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', OrLoOp], ['right', Number]]:
                left = self.convert_OrLoOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', String]]:
                left = self.convert_Index(node.left)
                right = self.convert_String(node.right)
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', AddOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Index], ['right', SubOp]]:
                left = self.convert_Index(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', AddOp], ['right', ULengthOP]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_ULengthOP(node.right)
            case [['left', Name], ['right', Name]]:
                left = self.convert_Name(node.left)
                right = self.convert_Name(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Name], ['right', SubOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Name], ['right', ULengthOP]]:
                left = self.convert_Name(node.left)
                right = self.convert_ULengthOP(node.right)
    case 'ModOp':
        match pattern:
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', Invoke], ['right', Number]]:
                left = self.convert_Invoke(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', AddOp]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', ULengthOP], ['right', Number]]:
                left = self.convert_ULengthOP(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', OrLoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_OrLoOp(node.right)
            case [['left', Name], ['right', Number]]:
                left = self.convert_Name(node.left)
                right = self.convert_Number(node.right)
            case [['left', MultOp], ['right', Number]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', Index]]:
                left = self.convert_Call(node.left)
                right = self.convert_Index(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', Index], ['right', Index]]:
                left = self.convert_Index(node.left)
                right = self.convert_Index(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Name], ['right', ExpoOp]]:
                left = self.convert_Name(node.left)
                right = self.convert_ExpoOp(node.right)
    case 'Break':
        match pattern:
            case []:
    case 'ExpoOp':
        match pattern:
            case [['left', Index], ['right', Number]]:
                left = self.convert_Index(node.left)
                right = self.convert_Number(node.right)
            case [['left', SubOp], ['right', Number]]:
                left = self.convert_SubOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', Call], ['right', SubOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_SubOp(node.right)
            case [['left', Call], ['right', AddOp]]:
                left = self.convert_Call(node.left)
                right = self.convert_AddOp(node.right)
            case [['left', Call], ['right', Number]]:
                left = self.convert_Call(node.left)
                right = self.convert_Number(node.right)
            case [['left', FloatDivOp], ['right', Number]]:
                left = self.convert_FloatDivOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Number]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Number(node.right)
            case [['left', AddOp], ['right', Name]]:
                left = self.convert_AddOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', MultOp], ['right', Name]]:
                left = self.convert_MultOp(node.left)
                right = self.convert_Name(node.right)
            case [['left', Number], ['right', Call]]:
                left = self.convert_Number(node.left)
                right = self.convert_Call(node.right)
            case [['left', Number], ['right', Name]]:
                left = self.convert_Number(node.left)
                right = self.convert_Name(node.right)
    case 'Function':
        match pattern:
            case [['name', Index], ['body', Block]]:
                name = self.convert_Index(node.name)
                body = self.convert_Block(node.body)
            case [['name', Name], ['body', Block]]:
                name = self.convert_Name(node.name)
                body = self.convert_Block(node.body)
    case 'LocalFunction':
        match pattern:
            case [['name', Name], ['body', Block]]:
                name = self.convert_Name(node.name)
                body = self.convert_Block(node.body)
    case 'Varargs':
        match pattern:
            case []: