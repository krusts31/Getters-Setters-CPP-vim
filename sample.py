import vim

def insert_class(arg, x):
	y = int(x)
	vim.current.window.cursor = (y , 0)
	out = "#ifndef " + vim.eval("a:arg") + "_CLASS_H"
	vim.current.line = out
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "# define " + vim.eval("a:arg") + "_CLASS_H"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "class " + vim.eval("a:arg") + "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "public:"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + vim.eval("a:arg") + "();"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	~" + vim.eval("a:arg") + "();"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + vim.eval("a:arg") + "(" + vim.eval("a:arg") + " const & src);"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  ""
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + vim.eval("a:arg") + " & operator=(" + vim.eval("a:arg") + " const & src);"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "};"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "#endif"

def deffine_class(arg, x):
	y = int(x)
	vim.current.window.cursor = (y , 0)
	vim.current.line = "#include \"" + vim.eval("a:arg") + ".hpp\""
	y = y + 1
	vim.current.window.cursor = (y , 0)
	vim.current.line =  vim.eval("a:arg") + "::" + vim.eval("a:arg") + "()"
	y = y + 1
	vim.current.window.cursor = (y , 0)
	vim.current.line =  "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + "return ;"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "}"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  vim.eval("a:arg") + "::~" + vim.eval("a:arg") + "()"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + "return ;"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "}"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  vim.eval("a:arg") + " & " + vim.eval("a:arg") + "::operator=(" + vim.eval("a:arg") + " const & src)"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "	" + "return *this;"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "}"

def insert_set_get(clas, var, typ, x):
	y = int(x)
	vim.current.window.cursor = (y, 0)
	vim.current.line = vim.eval("a:typ") + "	" + "get" + vim.eval("a:var") + "(void)		const;"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "void	" + "set" + vim.eval("a:var") + "(" + vim.eval("a:typ")  + " " + vim.eval("a:var") + ");"

def deffine_set_get (clas, var, typ, x):
	y = int(x)
	vim.current.window.cursor = (y, 0)
	vim.current.line = vim.eval("a:typ") + "	" + vim.eval("a:clas") + "::get" + vim.eval("a:var") + "(void) const"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "	return (this->_" + vim.eval("a:var") + ");"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "}"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line =  "void	" + vim.eval("a:clas") + "::set" + vim.eval("a:var") + "(" + vim.eval("a:typ")  + " " + vim.eval("a:var") + ")"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "{"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "	this->_" + vim.eval("a:var") + " = " + vim.eval("a:var") + ";"
	y = y + 1
	vim.current.window.cursor = (y, 0)
	vim.current.line = "}"
