-- Render GitHub-style alerts without changing ordinary quotes or code examples.
local alerts = {
  NOTE = {title = 'Hinweis', color = '1769aa'},
  TIP = {title = 'Tipp', color = '287a3d'},
  IMPORTANT = {title = 'Wichtig', color = '7650a6'},
  WARNING = {title = 'Warnung', color = '926400'},
  CAUTION = {title = 'Achtung', color = 'b42318'},
}

function BlockQuote(block)
  local first = block.content[1]
  if not first or (first.t ~= 'Para' and first.t ~= 'Plain') then return nil end
  local marker = first.content[1]
  if not marker or marker.t ~= 'Str' then return nil end
  local kind = marker.text:match('^%[!(%u+)%]$')
  local alert = alerts[kind]
  if not alert then return nil end
  -- The marker must occupy its own line.
  local separator = first.content[2]
  if separator and separator.t ~= 'SoftBreak' and separator.t ~= 'LineBreak' then
    return nil
  end
  first.content:remove(1)
  if separator then first.content:remove(1) end
  if #first.content == 0 then block.content:remove(1) end

  if FORMAT:match('html') then
    block.content:insert(1, pandoc.Div(
      {pandoc.Para({pandoc.Str(alert.title)})},
      pandoc.Attr('', {'alert-title'})
    ))
    return pandoc.Div(block.content, pandoc.Attr('', {'alert', 'alert-' .. kind:lower()}))
  elseif FORMAT:match('latex') then
    block.content:insert(1, pandoc.RawBlock('latex',
      '\\begin{docAlert}{' .. alert.color .. '}{' .. alert.title .. '}'))
    block.content:insert(pandoc.RawBlock('latex', '\\end{docAlert}'))
    return block.content
  end
end
