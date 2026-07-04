// Generated from c:/Users/100204924/Documents/tec/veranos/automatas2/git_automatas/antlr/Streamlint/e12/Expr.g4 by ANTLR 4.13.1
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
		PUBLIC=1, CLASS=2, STATIC=3, VOID=4, INT=5, IF=6, MAS=7, IGUAL=8, MAYOR_IGUAL=9, 
		PAR_IZQ=10, PAR_DER=11, LLAVE_IZQ=12, LLAVE_DER=13, COR_IZQ=14, COR_DER=15, 
		PUNTO_COMA=16, PUNTO=17, COMA=18, ENTERO=19, CADENA=20, IDENTIFICADOR=21, 
		WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PUBLIC", "CLASS", "STATIC", "VOID", "INT", "IF", "MAS", "IGUAL", "MAYOR_IGUAL", 
			"PAR_IZQ", "PAR_DER", "LLAVE_IZQ", "LLAVE_DER", "COR_IZQ", "COR_DER", 
			"PUNTO_COMA", "PUNTO", "COMA", "ENTERO", "CADENA", "IDENTIFICADOR", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'public'", "'class'", "'static'", "'void'", "'int'", "'if'", "'+'", 
			"'='", "'>='", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "'.'", 
			"','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PUBLIC", "CLASS", "STATIC", "VOID", "INT", "IF", "MAS", "IGUAL", 
			"MAYOR_IGUAL", "PAR_IZQ", "PAR_DER", "LLAVE_IZQ", "LLAVE_DER", "COR_IZQ", 
			"COR_DER", "PUNTO_COMA", "PUNTO", "COMA", "ENTERO", "CADENA", "IDENTIFICADOR", 
			"WS"
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
		"\u0004\u0000\u0016\u0082\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0004\u0012h\b\u0012\u000b\u0012\f\u0012"+
		"i\u0001\u0013\u0001\u0013\u0005\u0013n\b\u0013\n\u0013\f\u0013q\t\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0005\u0014w\b\u0014"+
		"\n\u0014\f\u0014z\t\u0014\u0001\u0015\u0004\u0015}\b\u0015\u000b\u0015"+
		"\f\u0015~\u0001\u0015\u0001\u0015\u0000\u0000\u0016\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010"+
		"!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001\u0000\u0005\u0001\u0000"+
		"09\u0003\u0000\n\n\r\r\"\"\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003"+
		"\u0000\t\n\r\r  \u0085\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000"+
		"\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000"+
		")\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0001-\u0001"+
		"\u0000\u0000\u0000\u00034\u0001\u0000\u0000\u0000\u0005:\u0001\u0000\u0000"+
		"\u0000\u0007A\u0001\u0000\u0000\u0000\tF\u0001\u0000\u0000\u0000\u000b"+
		"J\u0001\u0000\u0000\u0000\rM\u0001\u0000\u0000\u0000\u000fO\u0001\u0000"+
		"\u0000\u0000\u0011Q\u0001\u0000\u0000\u0000\u0013T\u0001\u0000\u0000\u0000"+
		"\u0015V\u0001\u0000\u0000\u0000\u0017X\u0001\u0000\u0000\u0000\u0019Z"+
		"\u0001\u0000\u0000\u0000\u001b\\\u0001\u0000\u0000\u0000\u001d^\u0001"+
		"\u0000\u0000\u0000\u001f`\u0001\u0000\u0000\u0000!b\u0001\u0000\u0000"+
		"\u0000#d\u0001\u0000\u0000\u0000%g\u0001\u0000\u0000\u0000\'k\u0001\u0000"+
		"\u0000\u0000)t\u0001\u0000\u0000\u0000+|\u0001\u0000\u0000\u0000-.\u0005"+
		"p\u0000\u0000./\u0005u\u0000\u0000/0\u0005b\u0000\u000001\u0005l\u0000"+
		"\u000012\u0005i\u0000\u000023\u0005c\u0000\u00003\u0002\u0001\u0000\u0000"+
		"\u000045\u0005c\u0000\u000056\u0005l\u0000\u000067\u0005a\u0000\u0000"+
		"78\u0005s\u0000\u000089\u0005s\u0000\u00009\u0004\u0001\u0000\u0000\u0000"+
		":;\u0005s\u0000\u0000;<\u0005t\u0000\u0000<=\u0005a\u0000\u0000=>\u0005"+
		"t\u0000\u0000>?\u0005i\u0000\u0000?@\u0005c\u0000\u0000@\u0006\u0001\u0000"+
		"\u0000\u0000AB\u0005v\u0000\u0000BC\u0005o\u0000\u0000CD\u0005i\u0000"+
		"\u0000DE\u0005d\u0000\u0000E\b\u0001\u0000\u0000\u0000FG\u0005i\u0000"+
		"\u0000GH\u0005n\u0000\u0000HI\u0005t\u0000\u0000I\n\u0001\u0000\u0000"+
		"\u0000JK\u0005i\u0000\u0000KL\u0005f\u0000\u0000L\f\u0001\u0000\u0000"+
		"\u0000MN\u0005+\u0000\u0000N\u000e\u0001\u0000\u0000\u0000OP\u0005=\u0000"+
		"\u0000P\u0010\u0001\u0000\u0000\u0000QR\u0005>\u0000\u0000RS\u0005=\u0000"+
		"\u0000S\u0012\u0001\u0000\u0000\u0000TU\u0005(\u0000\u0000U\u0014\u0001"+
		"\u0000\u0000\u0000VW\u0005)\u0000\u0000W\u0016\u0001\u0000\u0000\u0000"+
		"XY\u0005{\u0000\u0000Y\u0018\u0001\u0000\u0000\u0000Z[\u0005}\u0000\u0000"+
		"[\u001a\u0001\u0000\u0000\u0000\\]\u0005[\u0000\u0000]\u001c\u0001\u0000"+
		"\u0000\u0000^_\u0005]\u0000\u0000_\u001e\u0001\u0000\u0000\u0000`a\u0005"+
		";\u0000\u0000a \u0001\u0000\u0000\u0000bc\u0005.\u0000\u0000c\"\u0001"+
		"\u0000\u0000\u0000de\u0005,\u0000\u0000e$\u0001\u0000\u0000\u0000fh\u0007"+
		"\u0000\u0000\u0000gf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000"+
		"ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000j&\u0001\u0000\u0000"+
		"\u0000ko\u0005\"\u0000\u0000ln\b\u0001\u0000\u0000ml\u0001\u0000\u0000"+
		"\u0000nq\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000op\u0001\u0000"+
		"\u0000\u0000pr\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000rs\u0005"+
		"\"\u0000\u0000s(\u0001\u0000\u0000\u0000tx\u0007\u0002\u0000\u0000uw\u0007"+
		"\u0003\u0000\u0000vu\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000"+
		"xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000y*\u0001\u0000\u0000"+
		"\u0000zx\u0001\u0000\u0000\u0000{}\u0007\u0004\u0000\u0000|{\u0001\u0000"+
		"\u0000\u0000}~\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f"+
		"\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0081"+
		"\u0006\u0015\u0000\u0000\u0081,\u0001\u0000\u0000\u0000\u0005\u0000io"+
		"x~\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}