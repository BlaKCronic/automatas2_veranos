// Generated from c:/Users/100204924/Documents/tec/veranos/automatas2/git_automatas/antlr/Streamlint/e14/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		UPDATE=1, SET=2, WHERE=3, IGUAL=4, COMA=5, PUNTO_COMA=6, ENTERO=7, CADENA=8, 
		IDENTIFICADOR=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"UPDATE", "SET", "WHERE", "IGUAL", "COMA", "PUNTO_COMA", "ENTERO", "CADENA", 
			"IDENTIFICADOR", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'UPDATE'", "'SET'", "'WHERE'", "'='", "','", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "UPDATE", "SET", "WHERE", "IGUAL", "COMA", "PUNTO_COMA", "ENTERO", 
			"CADENA", "IDENTIFICADOR", "WS"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\nH\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0004\u0006.\b\u0006\u000b"+
		"\u0006\f\u0006/\u0001\u0007\u0001\u0007\u0005\u00074\b\u0007\n\u0007\f"+
		"\u00077\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0005\b=\b\b\n"+
		"\b\f\b@\t\b\u0001\t\u0004\tC\b\t\u000b\t\f\tD\u0001\t\u0001\t\u0000\u0000"+
		"\n\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0001\u0000\u0005\u0001\u000009\u0003"+
		"\u0000\n\n\r\r\'\'\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\t"+
		"\n\r\r  K\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0001\u0015\u0001\u0000\u0000\u0000\u0003\u001c\u0001\u0000\u0000\u0000"+
		"\u0005 \u0001\u0000\u0000\u0000\u0007&\u0001\u0000\u0000\u0000\t(\u0001"+
		"\u0000\u0000\u0000\u000b*\u0001\u0000\u0000\u0000\r-\u0001\u0000\u0000"+
		"\u0000\u000f1\u0001\u0000\u0000\u0000\u0011:\u0001\u0000\u0000\u0000\u0013"+
		"B\u0001\u0000\u0000\u0000\u0015\u0016\u0005U\u0000\u0000\u0016\u0017\u0005"+
		"P\u0000\u0000\u0017\u0018\u0005D\u0000\u0000\u0018\u0019\u0005A\u0000"+
		"\u0000\u0019\u001a\u0005T\u0000\u0000\u001a\u001b\u0005E\u0000\u0000\u001b"+
		"\u0002\u0001\u0000\u0000\u0000\u001c\u001d\u0005S\u0000\u0000\u001d\u001e"+
		"\u0005E\u0000\u0000\u001e\u001f\u0005T\u0000\u0000\u001f\u0004\u0001\u0000"+
		"\u0000\u0000 !\u0005W\u0000\u0000!\"\u0005H\u0000\u0000\"#\u0005E\u0000"+
		"\u0000#$\u0005R\u0000\u0000$%\u0005E\u0000\u0000%\u0006\u0001\u0000\u0000"+
		"\u0000&\'\u0005=\u0000\u0000\'\b\u0001\u0000\u0000\u0000()\u0005,\u0000"+
		"\u0000)\n\u0001\u0000\u0000\u0000*+\u0005;\u0000\u0000+\f\u0001\u0000"+
		"\u0000\u0000,.\u0007\u0000\u0000\u0000-,\u0001\u0000\u0000\u0000./\u0001"+
		"\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u0000"+
		"0\u000e\u0001\u0000\u0000\u000015\u0005\'\u0000\u000024\b\u0001\u0000"+
		"\u000032\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000"+
		"\u0000\u000056\u0001\u0000\u0000\u000068\u0001\u0000\u0000\u000075\u0001"+
		"\u0000\u0000\u000089\u0005\'\u0000\u00009\u0010\u0001\u0000\u0000\u0000"+
		":>\u0007\u0002\u0000\u0000;=\u0007\u0003\u0000\u0000<;\u0001\u0000\u0000"+
		"\u0000=@\u0001\u0000\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000"+
		"\u0000\u0000?\u0012\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"AC\u0007\u0004\u0000\u0000BA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000"+
		"\u0000DB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EF\u0001\u0000"+
		"\u0000\u0000FG\u0006\t\u0000\u0000G\u0014\u0001\u0000\u0000\u0000\u0005"+
		"\u0000/5>D\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}