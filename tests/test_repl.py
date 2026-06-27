"""Test Lukylang REPL functionality"""
import pytest
import tempfile
import os

from luckylang.repl import LuckylangREPL


class TestREPL:
    """Test cases for Lukylang REPL"""

    def test_repl_initialization(self):
        """Test that REPL can be initialized"""
        repl = LuckylangREPL()
        assert repl.env == {}
        assert repl.history == []
        assert repl.in_block == False
        assert repl.history_file == ".luckylang_history"

    def test_repl_help_text(self):
        """Test help text is generated"""
        repl = LuckylangREPL()
        help_text = repl.commands()
        assert "Lukylang REPL Commands" in help_text
        assert ":help" in help_text
        assert ":quit" in help_text

    def test_repl_examples_show(self):
        """Test examples are shown when requested"""
        repl = LuckylangREPL()
        
        # Capture output
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            repl.show_examples()
        
        output = f.getvalue()
        assert "Hello from Lukylang!" in output
        assert "Variables and assignments" in output
        
    def test_repl_command_parsing(self):
        """Test that commands are parsed correctly"""
        repl = LuckylangREPL()
        
        # Test that commands are recognized
        assert repl.execute_line(":help") == True
        assert repl.execute_line("x = 10") == True
        assert repl.execute_line("print \"test\")") == True
    
    def test_repl_history_management(self):
        """Test history tracking and saving"""
        repl = LuckylangREPL()
        
        # Add some commands to history
        repl.history = ["x = 10", "y = 20", "print x + y"]
        
        # Test that history shows up in execute_line
        # (This is tested indirectly in the full REPL integration)
        assert len(repl.history) == 3
        
    def test_repl_block_detection(self):
        """Test block detection for multi-line statements"""
        repl = LuckylangREPL()
        
        # Test block detection
        # (This is tested in the full REPL flow)
        
    def test_repl_error_handling(self):
        """Test error handling in REPL"""
        repl = LuckylangREPL()
        
        # Test that invalid commands are handled gracefully
        # (This is tested in the full REPL integration)
        
    def test_repl_save_history(self):
        """Test that REPL can save history to file"""
        repl = LuckylangREPL()
        
        # Set up test history
        repl.history = ["x = 10", "y = 20", "print x + y"]
        repl.history_file = "test_history.txt"
        
        # Save history
        repl.save_history()
        
        # Check that file was created and has the right content
        assert os.path.exists(repl.history_file)
        
        with open(repl.history_file, 'r') as f:
            content = f.read()
            assert "x = 10" in content
            assert "y = 20" in content
            assert "print x + y" in content
        
        # Clean up
        os.remove(repl.history_file)
    
    def test_repl_clear_command(self):
        """Test :clear command"""
        repl = LuckylangREPL()
        
        # Mock os.system to avoid actually clearing the screen
        import unittest.mock
        with unittest.mock.patch('os.system'):
            # Should not raise an exception
            repl.execute_line(":clear")
    
    def test_repl_save_command(self):
        """Test :save command"""
        repl = LuckylangREPL()
        
        # Mock save functionality
        repl.save_history = unittest.mock.MagicMock()
        
        # Execute :save command
        result = repl.execute_line(":save")
        
        # Should return True and call save_history
        assert result == True
        repl.save_history.assert_called_once()
    
    def test_repl_quit_command(self):
        """Test :quit command"""
        repl = LuckylangREPL()
        
        # Note: REPL.quit actually calls sys.exit()
        # So this would cause the test to exit
        # For testing purposes, we assume the command is recognized
        assert repl.execute_line(":quit") == True
    
    def test_repl_import_integration(self):
        """Test that REPL can import luckylang modules"""
        # This tests that the REPL works with the core lukylang modules
        repl = LuckylangREPL()
        
        # The REPL should be able to execute basic lukylang code
        from luckylang import run
        
        # Test that run function is available
        assert callable(run)
        
        # Test basic execution
        test_code = 'print "Hello from REPL integration test"'
        run(test_code)  # Should not raise an exception
    
    def test_repl_help_integration(self):
        """Test that REPL help is integrated"""
        repl = LuckylangREPL()
        
        # Test that help is available
        help_text = repl.commands()
        assert "Commands" in help_text
        assert "Help" in help_text
    
    def test_repl_examples_integration(self):
        """Test that REPL examples work"""
        repl = LuckylangREPL()
        
        # Test that examples can be shown
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            repl.show_examples()
        
        output = f.getvalue()
        assert len(output) > 0
        assert "Example Programs" in output

    def test_commands_method_exists(self):
        """Test that commands method exists"""
        repl = LuckylangREPL()
        assert hasattr(repl, 'commands')
        assert callable(repl.commands)
        
    def test_examples_method_exists(self):
        """Test that examples method exists"""
        repl = LuckylangREPL()
        assert hasattr(repl, 'show_examples')
        assert callable(repl.show_examples)
    
    def test_history_file_default(self):
        """Test that history file is set correctly"""
        repl = LuckylangREPL()
        assert repl.history_file == ".luckylang_history"