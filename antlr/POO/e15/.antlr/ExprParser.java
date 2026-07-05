// Generated from c:/Users/josue/OneDrive/Documentos/ejercicios_automatas/automatas2_veranos/antlr/POO/e15/Expr.g4 by ANTLR 4.13.1
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
		SUDO=1, NMAP=2, SS=3, TCPDUMP=4, CURL=5, DIG=6, JOURNALCTL=7, GREP=8, 
		UFW=9, OPTION=10, IP_CIDR=11, IP_ADDR=12, HOSTNAME=13, STRING=14, WORD=15, 
		SEMICOLON=16, WS=17;
	public static final int
		RULE_program = 0, RULE_commandLine = 1, RULE_command = 2, RULE_sudo = 3, 
		RULE_baseCommand = 4, RULE_arg = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "commandLine", "command", "sudo", "baseCommand", "arg"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'sudo'", "'nmap'", "'ss'", "'tcpdump'", "'curl'", "'dig'", "'journalctl'", 
			"'grep'", "'ufw'", null, null, null, null, null, null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SUDO", "NMAP", "SS", "TCPDUMP", "CURL", "DIG", "JOURNALCTL", "GREP", 
			"UFW", "OPTION", "IP_CIDR", "IP_ADDR", "HOSTNAME", "STRING", "WORD", 
			"SEMICOLON", "WS"
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
		public List<CommandLineContext> commandLine() {
			return getRuleContexts(CommandLineContext.class);
		}
		public CommandLineContext commandLine(int i) {
			return getRuleContext(CommandLineContext.class,i);
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
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1022L) != 0)) {
				{
				{
				setState(12);
				commandLine();
				}
				}
				setState(17);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(18);
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
	public static class CommandLineContext extends ParserRuleContext {
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public CommandLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commandLine; }
	}

	public final CommandLineContext commandLine() throws RecognitionException {
		CommandLineContext _localctx = new CommandLineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_commandLine);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			command();
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(21);
				match(SEMICOLON);
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
	public static class CommandContext extends ParserRuleContext {
		public BaseCommandContext baseCommand() {
			return getRuleContext(BaseCommandContext.class,0);
		}
		public SudoContext sudo() {
			return getRuleContext(SudoContext.class,0);
		}
		public List<ArgContext> arg() {
			return getRuleContexts(ArgContext.class);
		}
		public ArgContext arg(int i) {
			return getRuleContext(ArgContext.class,i);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_command);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SUDO) {
				{
				setState(24);
				sudo();
				}
			}

			setState(27);
			baseCommand();
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 64512L) != 0)) {
				{
				{
				setState(28);
				arg();
				}
				}
				setState(33);
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
	public static class SudoContext extends ParserRuleContext {
		public TerminalNode SUDO() { return getToken(ExprParser.SUDO, 0); }
		public SudoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sudo; }
	}

	public final SudoContext sudo() throws RecognitionException {
		SudoContext _localctx = new SudoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_sudo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(SUDO);
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
	public static class BaseCommandContext extends ParserRuleContext {
		public TerminalNode NMAP() { return getToken(ExprParser.NMAP, 0); }
		public TerminalNode SS() { return getToken(ExprParser.SS, 0); }
		public TerminalNode TCPDUMP() { return getToken(ExprParser.TCPDUMP, 0); }
		public TerminalNode CURL() { return getToken(ExprParser.CURL, 0); }
		public TerminalNode DIG() { return getToken(ExprParser.DIG, 0); }
		public TerminalNode JOURNALCTL() { return getToken(ExprParser.JOURNALCTL, 0); }
		public TerminalNode GREP() { return getToken(ExprParser.GREP, 0); }
		public TerminalNode UFW() { return getToken(ExprParser.UFW, 0); }
		public BaseCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_baseCommand; }
	}

	public final BaseCommandContext baseCommand() throws RecognitionException {
		BaseCommandContext _localctx = new BaseCommandContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_baseCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1020L) != 0)) ) {
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
	public static class ArgContext extends ParserRuleContext {
		public TerminalNode OPTION() { return getToken(ExprParser.OPTION, 0); }
		public TerminalNode IP_CIDR() { return getToken(ExprParser.IP_CIDR, 0); }
		public TerminalNode IP_ADDR() { return getToken(ExprParser.IP_ADDR, 0); }
		public TerminalNode HOSTNAME() { return getToken(ExprParser.HOSTNAME, 0); }
		public TerminalNode STRING() { return getToken(ExprParser.STRING, 0); }
		public TerminalNode WORD() { return getToken(ExprParser.WORD, 0); }
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_arg);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 64512L) != 0)) ) {
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

	public static final String _serializedATN =
		"\u0004\u0001\u0011)\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0005\u0000\u000e\b\u0000\n\u0000\f\u0000"+
		"\u0011\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0017\b\u0001\u0001\u0002\u0003\u0002\u001a\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0005\u0002\u001e\b\u0002\n\u0002\f\u0002!\t\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0000\u0000\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0002\u0001\u0000"+
		"\u0002\t\u0001\u0000\n\u000f&\u0000\u000f\u0001\u0000\u0000\u0000\u0002"+
		"\u0014\u0001\u0000\u0000\u0000\u0004\u0019\u0001\u0000\u0000\u0000\u0006"+
		"\"\u0001\u0000\u0000\u0000\b$\u0001\u0000\u0000\u0000\n&\u0001\u0000\u0000"+
		"\u0000\f\u000e\u0003\u0002\u0001\u0000\r\f\u0001\u0000\u0000\u0000\u000e"+
		"\u0011\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f\u0010"+
		"\u0001\u0000\u0000\u0000\u0010\u0012\u0001\u0000\u0000\u0000\u0011\u000f"+
		"\u0001\u0000\u0000\u0000\u0012\u0013\u0005\u0000\u0000\u0001\u0013\u0001"+
		"\u0001\u0000\u0000\u0000\u0014\u0016\u0003\u0004\u0002\u0000\u0015\u0017"+
		"\u0005\u0010\u0000\u0000\u0016\u0015\u0001\u0000\u0000\u0000\u0016\u0017"+
		"\u0001\u0000\u0000\u0000\u0017\u0003\u0001\u0000\u0000\u0000\u0018\u001a"+
		"\u0003\u0006\u0003\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u0019\u001a"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000\u0000\u0000\u001b\u001f"+
		"\u0003\b\u0004\u0000\u001c\u001e\u0003\n\u0005\u0000\u001d\u001c\u0001"+
		"\u0000\u0000\u0000\u001e!\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000"+
		"\u0000\u0000\u001f \u0001\u0000\u0000\u0000 \u0005\u0001\u0000\u0000\u0000"+
		"!\u001f\u0001\u0000\u0000\u0000\"#\u0005\u0001\u0000\u0000#\u0007\u0001"+
		"\u0000\u0000\u0000$%\u0007\u0000\u0000\u0000%\t\u0001\u0000\u0000\u0000"+
		"&\'\u0007\u0001\u0000\u0000\'\u000b\u0001\u0000\u0000\u0000\u0004\u000f"+
		"\u0016\u0019\u001f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}