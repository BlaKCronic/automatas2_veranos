// Generated from c:/Users/josue/OneDrive/Documentos/ejercicios_automatas/automatas2_veranos/antlr/POO/e13/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CREATE=1, TABLE=2, INSERT=3, INTO=4, VALUES=5, SELECT=6, FROM=7, INNER=8, 
		JOIN=9, ON=10, WHERE=11, SERIAL=12, INTEGER=13, VARCHAR=14, DATE=15, PRIMARY=16, 
		KEY=17, NOT=18, NULL=19, EQ=20, LPAREN=21, RPAREN=22, COMMA=23, SEMICOLON=24, 
		DOT=25, STRING=26, ID=27, NUM=28, WS=29;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_createTableStmt = 2, RULE_columnDef = 3, 
		RULE_typeDef = 4, RULE_columnConstraint = 5, RULE_insertStmt = 6, RULE_valueList = 7, 
		RULE_literalValue = 8, RULE_selectStmt = 9, RULE_selectItem = 10, RULE_tableRef = 11, 
		RULE_alias = 12, RULE_condition = 13, RULE_valueExpr = 14, RULE_columnName = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "createTableStmt", "columnDef", "typeDef", "columnConstraint", 
			"insertStmt", "valueList", "literalValue", "selectStmt", "selectItem", 
			"tableRef", "alias", "condition", "valueExpr", "columnName"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'CREATE'", "'TABLE'", "'INSERT'", "'INTO'", "'VALUES'", "'SELECT'", 
			"'FROM'", "'INNER'", "'JOIN'", "'ON'", "'WHERE'", "'SERIAL'", "'INTEGER'", 
			"'VARCHAR'", "'DATE'", "'PRIMARY'", "'KEY'", "'NOT'", "'NULL'", "'='", 
			"'('", "')'", "','", "';'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CREATE", "TABLE", "INSERT", "INTO", "VALUES", "SELECT", "FROM", 
			"INNER", "JOIN", "ON", "WHERE", "SERIAL", "INTEGER", "VARCHAR", "DATE", 
			"PRIMARY", "KEY", "NOT", "NULL", "EQ", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
			"DOT", "STRING", "ID", "NUM", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 74L) != 0)) {
				{
				{
				setState(32);
				statement();
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public CreateTableStmtContext createTableStmt() {
			return getRuleContext(CreateTableStmtContext.class,0);
		}
		public InsertStmtContext insertStmt() {
			return getRuleContext(InsertStmtContext.class,0);
		}
		public SelectStmtContext selectStmt() {
			return getRuleContext(SelectStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				createTableStmt();
				}
				break;
			case INSERT:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				insertStmt();
				}
				break;
			case SELECT:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				selectStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateTableStmtContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(ExprParser.CREATE, 0); }
		public TerminalNode TABLE() { return getToken(ExprParser.TABLE, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public List<ColumnDefContext> columnDef() {
			return getRuleContexts(ColumnDefContext.class);
		}
		public ColumnDefContext columnDef(int i) {
			return getRuleContext(ColumnDefContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public CreateTableStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createTableStmt; }
	}

	public final CreateTableStmtContext createTableStmt() throws RecognitionException {
		CreateTableStmtContext _localctx = new CreateTableStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_createTableStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(CREATE);
			setState(46);
			match(TABLE);
			setState(47);
			match(ID);
			setState(48);
			match(LPAREN);
			setState(49);
			columnDef();
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(50);
				match(COMMA);
				setState(51);
				columnDef();
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			match(RPAREN);
			setState(58);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColumnDefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public TypeDefContext typeDef() {
			return getRuleContext(TypeDefContext.class,0);
		}
		public List<ColumnConstraintContext> columnConstraint() {
			return getRuleContexts(ColumnConstraintContext.class);
		}
		public ColumnConstraintContext columnConstraint(int i) {
			return getRuleContext(ColumnConstraintContext.class,i);
		}
		public ColumnDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_columnDef; }
	}

	public final ColumnDefContext columnDef() throws RecognitionException {
		ColumnDefContext _localctx = new ColumnDefContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_columnDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(ID);
			setState(61);
			typeDef();
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PRIMARY || _la==NOT) {
				{
				{
				setState(62);
				columnConstraint();
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeDefContext extends ParserRuleContext {
		public TerminalNode SERIAL() { return getToken(ExprParser.SERIAL, 0); }
		public TerminalNode INTEGER() { return getToken(ExprParser.INTEGER, 0); }
		public TerminalNode VARCHAR() { return getToken(ExprParser.VARCHAR, 0); }
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public TerminalNode NUM() { return getToken(ExprParser.NUM, 0); }
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public TerminalNode DATE() { return getToken(ExprParser.DATE, 0); }
		public TypeDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeDef; }
	}

	public final TypeDefContext typeDef() throws RecognitionException {
		TypeDefContext _localctx = new TypeDefContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typeDef);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SERIAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				match(SERIAL);
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				match(INTEGER);
				}
				break;
			case VARCHAR:
				enterOuterAlt(_localctx, 3);
				{
				setState(70);
				match(VARCHAR);
				setState(71);
				match(LPAREN);
				setState(72);
				match(NUM);
				setState(73);
				match(RPAREN);
				}
				break;
			case DATE:
				enterOuterAlt(_localctx, 4);
				{
				setState(74);
				match(DATE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColumnConstraintContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(ExprParser.NOT, 0); }
		public TerminalNode NULL() { return getToken(ExprParser.NULL, 0); }
		public TerminalNode PRIMARY() { return getToken(ExprParser.PRIMARY, 0); }
		public TerminalNode KEY() { return getToken(ExprParser.KEY, 0); }
		public ColumnConstraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_columnConstraint; }
	}

	public final ColumnConstraintContext columnConstraint() throws RecognitionException {
		ColumnConstraintContext _localctx = new ColumnConstraintContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_columnConstraint);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(NOT);
				setState(78);
				match(NULL);
				}
				break;
			case PRIMARY:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				match(PRIMARY);
				setState(80);
				match(KEY);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InsertStmtContext extends ParserRuleContext {
		public TerminalNode INSERT() { return getToken(ExprParser.INSERT, 0); }
		public TerminalNode INTO() { return getToken(ExprParser.INTO, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public List<ColumnNameContext> columnName() {
			return getRuleContexts(ColumnNameContext.class);
		}
		public ColumnNameContext columnName(int i) {
			return getRuleContext(ColumnNameContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public TerminalNode VALUES() { return getToken(ExprParser.VALUES, 0); }
		public List<ValueListContext> valueList() {
			return getRuleContexts(ValueListContext.class);
		}
		public ValueListContext valueList(int i) {
			return getRuleContext(ValueListContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public InsertStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_insertStmt; }
	}

	public final InsertStmtContext insertStmt() throws RecognitionException {
		InsertStmtContext _localctx = new InsertStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_insertStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(INSERT);
			setState(84);
			match(INTO);
			setState(85);
			match(ID);
			setState(86);
			match(LPAREN);
			setState(87);
			columnName();
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(88);
				match(COMMA);
				setState(89);
				columnName();
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(95);
			match(RPAREN);
			setState(96);
			match(VALUES);
			setState(97);
			valueList();
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(98);
				match(COMMA);
				setState(99);
				valueList();
				}
				}
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(105);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueListContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public List<LiteralValueContext> literalValue() {
			return getRuleContexts(LiteralValueContext.class);
		}
		public LiteralValueContext literalValue(int i) {
			return getRuleContext(LiteralValueContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public ValueListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valueList; }
	}

	public final ValueListContext valueList() throws RecognitionException {
		ValueListContext _localctx = new ValueListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_valueList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(LPAREN);
			setState(108);
			literalValue();
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(109);
				match(COMMA);
				setState(110);
				literalValue();
				}
				}
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(116);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(ExprParser.STRING, 0); }
		public TerminalNode NUM() { return getToken(ExprParser.NUM, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public LiteralValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalValue; }
	}

	public final LiteralValueContext literalValue() throws RecognitionException {
		LiteralValueContext _localctx = new LiteralValueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_literalValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 469762048L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectStmtContext extends ParserRuleContext {
		public TerminalNode SELECT() { return getToken(ExprParser.SELECT, 0); }
		public List<SelectItemContext> selectItem() {
			return getRuleContexts(SelectItemContext.class);
		}
		public SelectItemContext selectItem(int i) {
			return getRuleContext(SelectItemContext.class,i);
		}
		public TerminalNode FROM() { return getToken(ExprParser.FROM, 0); }
		public List<TableRefContext> tableRef() {
			return getRuleContexts(TableRefContext.class);
		}
		public TableRefContext tableRef(int i) {
			return getRuleContext(TableRefContext.class,i);
		}
		public TerminalNode WHERE() { return getToken(ExprParser.WHERE, 0); }
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public TerminalNode INNER() { return getToken(ExprParser.INNER, 0); }
		public TerminalNode JOIN() { return getToken(ExprParser.JOIN, 0); }
		public TerminalNode ON() { return getToken(ExprParser.ON, 0); }
		public SelectStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectStmt; }
	}

	public final SelectStmtContext selectStmt() throws RecognitionException {
		SelectStmtContext _localctx = new SelectStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_selectStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(SELECT);
			setState(121);
			selectItem();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(122);
				match(COMMA);
				setState(123);
				selectItem();
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(129);
			match(FROM);
			setState(130);
			tableRef();
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INNER) {
				{
				setState(131);
				match(INNER);
				setState(132);
				match(JOIN);
				setState(133);
				tableRef();
				setState(134);
				match(ON);
				setState(135);
				condition();
				}
			}

			setState(139);
			match(WHERE);
			setState(140);
			condition();
			setState(141);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectItemContext extends ParserRuleContext {
		public ColumnNameContext columnName() {
			return getRuleContext(ColumnNameContext.class,0);
		}
		public SelectItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectItem; }
	}

	public final SelectItemContext selectItem() throws RecognitionException {
		SelectItemContext _localctx = new SelectItemContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_selectItem);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			columnName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TableRefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public AliasContext alias() {
			return getRuleContext(AliasContext.class,0);
		}
		public TableRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableRef; }
	}

	public final TableRefContext tableRef() throws RecognitionException {
		TableRefContext _localctx = new TableRefContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_tableRef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(ID);
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(146);
				alias();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AliasContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public AliasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alias; }
	}

	public final AliasContext alias() throws RecognitionException {
		AliasContext _localctx = new AliasContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_alias);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ColumnNameContext columnName() {
			return getRuleContext(ColumnNameContext.class,0);
		}
		public TerminalNode EQ() { return getToken(ExprParser.EQ, 0); }
		public ValueExprContext valueExpr() {
			return getRuleContext(ValueExprContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			columnName();
			setState(152);
			match(EQ);
			setState(153);
			valueExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueExprContext extends ParserRuleContext {
		public LiteralValueContext literalValue() {
			return getRuleContext(LiteralValueContext.class,0);
		}
		public ColumnNameContext columnName() {
			return getRuleContext(ColumnNameContext.class,0);
		}
		public ValueExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valueExpr; }
	}

	public final ValueExprContext valueExpr() throws RecognitionException {
		ValueExprContext _localctx = new ValueExprContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_valueExpr);
		try {
			setState(157);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(155);
				literalValue();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				columnName();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColumnNameContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ExprParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ExprParser.ID, i);
		}
		public List<TerminalNode> DOT() { return getTokens(ExprParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(ExprParser.DOT, i);
		}
		public ColumnNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_columnName; }
	}

	public final ColumnNameContext columnName() throws RecognitionException {
		ColumnNameContext _localctx = new ColumnNameContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_columnName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(ID);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(160);
				match(DOT);
				setState(161);
				match(ID);
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001d\u00a8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0001\u0000\u0005\u0000\"\b\u0000\n\u0000\f\u0000%\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001,\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0005\u00025\b\u0002\n\u0002\f\u00028\t\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0005"+
		"\u0003@\b\u0003\n\u0003\f\u0003C\t\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004L\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005R\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0005\u0006[\b\u0006\n\u0006\f\u0006^\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006e\b"+
		"\u0006\n\u0006\f\u0006h\t\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u0007p\b\u0007\n\u0007\f\u0007s\t"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0005\t}\b\t\n\t\f\t\u0080\t\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u008a\b\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0003\u000b\u0094\b"+
		"\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u009e\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005"+
		"\u000f\u00a3\b\u000f\n\u000f\f\u000f\u00a6\t\u000f\u0001\u000f\u0000\u0000"+
		"\u0010\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e\u0000\u0001\u0001\u0000\u001a\u001c\u00a8\u0000#\u0001"+
		"\u0000\u0000\u0000\u0002+\u0001\u0000\u0000\u0000\u0004-\u0001\u0000\u0000"+
		"\u0000\u0006<\u0001\u0000\u0000\u0000\bK\u0001\u0000\u0000\u0000\nQ\u0001"+
		"\u0000\u0000\u0000\fS\u0001\u0000\u0000\u0000\u000ek\u0001\u0000\u0000"+
		"\u0000\u0010v\u0001\u0000\u0000\u0000\u0012x\u0001\u0000\u0000\u0000\u0014"+
		"\u008f\u0001\u0000\u0000\u0000\u0016\u0091\u0001\u0000\u0000\u0000\u0018"+
		"\u0095\u0001\u0000\u0000\u0000\u001a\u0097\u0001\u0000\u0000\u0000\u001c"+
		"\u009d\u0001\u0000\u0000\u0000\u001e\u009f\u0001\u0000\u0000\u0000 \""+
		"\u0003\u0002\u0001\u0000! \u0001\u0000\u0000\u0000\"%\u0001\u0000\u0000"+
		"\u0000#!\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$&\u0001\u0000"+
		"\u0000\u0000%#\u0001\u0000\u0000\u0000&\'\u0005\u0000\u0000\u0001\'\u0001"+
		"\u0001\u0000\u0000\u0000(,\u0003\u0004\u0002\u0000),\u0003\f\u0006\u0000"+
		"*,\u0003\u0012\t\u0000+(\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		"+*\u0001\u0000\u0000\u0000,\u0003\u0001\u0000\u0000\u0000-.\u0005\u0001"+
		"\u0000\u0000./\u0005\u0002\u0000\u0000/0\u0005\u001b\u0000\u000001\u0005"+
		"\u0015\u0000\u000016\u0003\u0006\u0003\u000023\u0005\u0017\u0000\u0000"+
		"35\u0003\u0006\u0003\u000042\u0001\u0000\u0000\u000058\u0001\u0000\u0000"+
		"\u000064\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000079\u0001\u0000"+
		"\u0000\u000086\u0001\u0000\u0000\u00009:\u0005\u0016\u0000\u0000:;\u0005"+
		"\u0018\u0000\u0000;\u0005\u0001\u0000\u0000\u0000<=\u0005\u001b\u0000"+
		"\u0000=A\u0003\b\u0004\u0000>@\u0003\n\u0005\u0000?>\u0001\u0000\u0000"+
		"\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001\u0000"+
		"\u0000\u0000B\u0007\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"DL\u0005\f\u0000\u0000EL\u0005\r\u0000\u0000FG\u0005\u000e\u0000\u0000"+
		"GH\u0005\u0015\u0000\u0000HI\u0005\u001c\u0000\u0000IL\u0005\u0016\u0000"+
		"\u0000JL\u0005\u000f\u0000\u0000KD\u0001\u0000\u0000\u0000KE\u0001\u0000"+
		"\u0000\u0000KF\u0001\u0000\u0000\u0000KJ\u0001\u0000\u0000\u0000L\t\u0001"+
		"\u0000\u0000\u0000MN\u0005\u0012\u0000\u0000NR\u0005\u0013\u0000\u0000"+
		"OP\u0005\u0010\u0000\u0000PR\u0005\u0011\u0000\u0000QM\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000R\u000b\u0001\u0000\u0000\u0000ST\u0005"+
		"\u0003\u0000\u0000TU\u0005\u0004\u0000\u0000UV\u0005\u001b\u0000\u0000"+
		"VW\u0005\u0015\u0000\u0000W\\\u0003\u001e\u000f\u0000XY\u0005\u0017\u0000"+
		"\u0000Y[\u0003\u001e\u000f\u0000ZX\u0001\u0000\u0000\u0000[^\u0001\u0000"+
		"\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_`\u0005\u0016\u0000\u0000"+
		"`a\u0005\u0005\u0000\u0000af\u0003\u000e\u0007\u0000bc\u0005\u0017\u0000"+
		"\u0000ce\u0003\u000e\u0007\u0000db\u0001\u0000\u0000\u0000eh\u0001\u0000"+
		"\u0000\u0000fd\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000gi\u0001"+
		"\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000ij\u0005\u0018\u0000\u0000"+
		"j\r\u0001\u0000\u0000\u0000kl\u0005\u0015\u0000\u0000lq\u0003\u0010\b"+
		"\u0000mn\u0005\u0017\u0000\u0000np\u0003\u0010\b\u0000om\u0001\u0000\u0000"+
		"\u0000ps\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000qr\u0001\u0000"+
		"\u0000\u0000rt\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000tu\u0005"+
		"\u0016\u0000\u0000u\u000f\u0001\u0000\u0000\u0000vw\u0007\u0000\u0000"+
		"\u0000w\u0011\u0001\u0000\u0000\u0000xy\u0005\u0006\u0000\u0000y~\u0003"+
		"\u0014\n\u0000z{\u0005\u0017\u0000\u0000{}\u0003\u0014\n\u0000|z\u0001"+
		"\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000"+
		"\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0081\u0001\u0000\u0000\u0000"+
		"\u0080~\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u0007\u0000\u0000\u0082"+
		"\u0089\u0003\u0016\u000b\u0000\u0083\u0084\u0005\b\u0000\u0000\u0084\u0085"+
		"\u0005\t\u0000\u0000\u0085\u0086\u0003\u0016\u000b\u0000\u0086\u0087\u0005"+
		"\n\u0000\u0000\u0087\u0088\u0003\u001a\r\u0000\u0088\u008a\u0001\u0000"+
		"\u0000\u0000\u0089\u0083\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000"+
		"\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u000b"+
		"\u0000\u0000\u008c\u008d\u0003\u001a\r\u0000\u008d\u008e\u0005\u0018\u0000"+
		"\u0000\u008e\u0013\u0001\u0000\u0000\u0000\u008f\u0090\u0003\u001e\u000f"+
		"\u0000\u0090\u0015\u0001\u0000\u0000\u0000\u0091\u0093\u0005\u001b\u0000"+
		"\u0000\u0092\u0094\u0003\u0018\f\u0000\u0093\u0092\u0001\u0000\u0000\u0000"+
		"\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0017\u0001\u0000\u0000\u0000"+
		"\u0095\u0096\u0005\u001b\u0000\u0000\u0096\u0019\u0001\u0000\u0000\u0000"+
		"\u0097\u0098\u0003\u001e\u000f\u0000\u0098\u0099\u0005\u0014\u0000\u0000"+
		"\u0099\u009a\u0003\u001c\u000e\u0000\u009a\u001b\u0001\u0000\u0000\u0000"+
		"\u009b\u009e\u0003\u0010\b\u0000\u009c\u009e\u0003\u001e\u000f\u0000\u009d"+
		"\u009b\u0001\u0000\u0000\u0000\u009d\u009c\u0001\u0000\u0000\u0000\u009e"+
		"\u001d\u0001\u0000\u0000\u0000\u009f\u00a4\u0005\u001b\u0000\u0000\u00a0"+
		"\u00a1\u0005\u0019\u0000\u0000\u00a1\u00a3\u0005\u001b\u0000\u0000\u00a2"+
		"\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5"+
		"\u001f\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u000e"+
		"#+6AKQ\\fq~\u0089\u0093\u009d\u00a4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}